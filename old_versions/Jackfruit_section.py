#!/usr/bin/env python3

# This is a series of functions for parsing motif disruptions in a vcf
# Jackfruit is for snps only. Indels (Durian) are coming
# It uses the JASPAR database for degenerate consensus motifs

# Testing Usage:
	# ./Jackfruit.py <JASPAR_file> <VCF> <Reference_Fasta> <slop_len>


import sys
import re
from Bio import motifs
from VCBerry import *
import pybedtools

# Take in JASPAR matrices and parse to a dict
# From JASPAR download non-redundant single batch pfms
def parse_JASPAR(jaspar_matrices_file):
	IUPAC_dict = {'R':'[AG]', 'Y':'[CT]', 'S':'[GC]',
	'W':'[AT]', 'K':'[GT]', 'M':'[AC]', 'B':'[CGT]',
	'D':'[AGT]', 'H':'[ACT]', 'V':'[ACG]', 'N':'[ACGT]'} # For degenerate consensus regex
	JASPAR_dict = {}
	with open(jaspar_matrices_file, 'r') as matrices:
		for matrix in motifs.parse(matrices, 'jaspar'): # function from Bio.motifs
			motif_counts = matrix.counts # Bio.motifs
			consensus = str(motif_counts.degenerate_consensus)
			consensus = consensus.replace('N','') # Ns in consensus are not useful downstream
			motif_name = matrix.name
			for code in IUPAC_dict:
				consensus = consensus.replace(code, IUPAC_dict[code]) # make consensus regexable
			JASPAR_dict[motif_name]=consensus
	return JASPAR_dict

# From pd.DataFrame, use pybedtools to make a bed file
# Assumes specific column names, which are relatively standard
def make_bed(VCBerry_df, slop_len=15):
	bed_frame = pd.DataFrame() # Empty df
	bed_frame['chrom'] = VCBerry_df['CHROM'] # Put VCBerry columns in bed order
	bed_frame['start'] = VCBerry_df['POS'] - slop_len # similar to bedtools slop
	bed_frame['stop'] = VCBerry_df['POS'] + slop_len
	bed_frame['CHROM_POS'] = VCBerry_df['CHROM_POS']
	bed = pybedtools.BedTool.from_dataframe(bed_frame) # pybedtools function
	return bed

# Using bed file from above with reference fa, make a fasta dictionary
def get_fasta(VCBerry_df, bed, ref_fa):
	Jackfruit_bed = bed.sequence(fi=ref_fa) # pybedtools function
	fasta_str = open(Jackfruit_bed.seqfn).read() # the above basically makes one string
	fasta_list = fasta_str.split('\n')[:-1] # split on newlines, remove empty last row
	fasta_dict = {}
	i=0
	fasta_list_it= iter(fasta_list)
	try:
		while True:
			line = next(fasta_list_it)
			if line.startswith('>'): # I don't like their headers, but ID that it's here
				header = VCBerry_df.iloc[i]['CHROM_POS'] # Reassign fasta header to chrom_pos
				i += 1
			else:
				fasta_dict[header] = line.upper() # for consistency, to upper
	except StopIteration:
		pass
	return fasta_dict

# Small function to loop through JASPAR and put found motifs in a set
# using re.search will be a problem if your slop length is too big
def motif_search(sequence, JASPAR_dict):
	motifs_set = set()
	for motif in JASPAR_dict:
		if re.search(JASPAR_dict[motif], sequence):
			motifs_set.add(motif)
	return motifs_set

# The big one
# This does four things:
	# Gets sequence context for a snp (make_bed and get_fasta)
	# Makes substitutions according to variants identified
	# Looks for motifs in ref and alt sequences (motif_search)
	# Determines which motifs change with the snp
def seq_disruptor(fasta_dict, VCBerry_df, JASPAR_dict, slop_len=15): # Obviously takes a few args
	find_replace_dict = {}
	fasta_keys_it = iter(fasta_dict.keys())
	try:
		while True:
			item = next(fasta_keys_it)
			df_slice = VCBerry_df.loc[VCBerry_df['CHROM_POS'] == item] # Find the origin line for sequence
			ref = df_slice.iloc[0]['REF'] # get nts
			alt = df_slice.iloc[0]['ALT']
			ref_seq = fasta_dict[item] # get sequence
			ref_motifs = motif_search(ref_seq, JASPAR_dict) # makes set of motifs in ref_seq
			if ',' in alt: # some snps have multiple alts
				alt_list = alt.split(',') # make them into a list
				for var in alt_list:
					header = item + '_' + ref + '>' + var # header for eventual dictionary
					find_replace_dict[header] = {}
					#print(f'Expected_ref: {ref} | Inserted_alt: {alt}') 
					#print(fasta_dict[item][:slop_len-1]+ var+fasta_dict[item][slop_len:] )
					#print(fasta_dict[item])
					alt_seq = fasta_dict[item][:slop_len-1]+ var +fasta_dict[item][slop_len:] # make snp
					find_replace_dict[header]['ref'] = ref_seq # put seqs in dictionary
					find_replace_dict[header]['alt'] = alt_seq
					alt_motifs = motif_search(alt_seq, JASPAR_dict) # set of motifs in alt_seq
					disrupted_motifs = ref_motifs - alt_motifs # set math
					gained_motifs = alt_motifs - ref_motifs
					find_replace_dict[header]['disrupted_motifs'] = disrupted_motifs # put uniques in dict
					find_replace_dict[header]['gained_motifs'] = gained_motifs
			else: # do the same for single variant alts
				header = item + '_' + ref + '>' + alt
				find_replace_dict[header] = {}
				alt_seq = fasta_dict[item][:slop_len-1]+ alt +fasta_dict[item][slop_len:]
				find_replace_dict[header]['ref'] = ref_seq
				find_replace_dict[header]['alt'] = alt_seq
				alt_motifs = motif_search(alt_seq, JASPAR_dict)
				disrupted_motifs = ref_motifs - alt_motifs
				gained_motifs = alt_motifs - ref_motifs
				find_replace_dict[header]['disrupted_motifs'] = disrupted_motifs
				find_replace_dict[header]['gained_motifs'] = gained_motifs
	except StopIteration:
		pass
	return find_replace_dict

# Testing the functionality of the Jackfruit pipeline
def main():
	file = sys.argv[1] # poorly named JASPAR file
	vcf_file = sys.argv[2]
	slop_len = int(sys.argv[4]) # How much to offset pos by
	JASPAR_dict = parse_JASPAR(file)
	Jackfruit = VCBerry(vcf_file)
	Jackfruit_bed = make_bed(Jackfruit.snps)
	#print(Jackfruit_bed)
	Hg38 = pybedtools.example_filename(sys.argv[3]) # ref fasta consistent with vcf input
	fasta_dict = get_fasta(Jackfruit.snps, Jackfruit_bed, Hg38)
	#print(fasta_dict)
	#print(JASPAR_dict)
	find_replace_dict = seq_disruptor(fasta_dict, Jackfruit.snps, JASPAR_dict, slop_len)
	for snp in find_replace_dict: # print dictionary all pretty
		print(snp)
		print(f'Reference sequence: {find_replace_dict[snp]["ref"]}')
		print(f'Alternate sequence: {find_replace_dict[snp]["alt"]}')
		print(f'Disrupted Motifs: {find_replace_dict[snp]["disrupted_motifs"]}')
		print(f'Gained Motifs: {find_replace_dict[snp]["gained_motifs"]}')
		print('\n')

if __name__ == '__main__':
	main()
