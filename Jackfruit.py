#!/usr/bin/env python3

#This will be at least one function used for parsing the JASPAR database for degenerate consensus motifs
#and also for searching sequences for motifs
# I could include the functionality for iterating through variants and making the sequences
import sys
import re
from Bio import motifs
from VCBerry import *
import pybedtools

def parse_JASPAR(jaspar_matrices_file):
	IUPAC_dict = {'R':'[AG]', 'Y':'[CT]', 'S':'[GC]',
	'W':'[AT]', 'K':'[GT]', 'M':'[AC]', 'B':'[CGT]',
	'D':'[AGT]', 'H':'[ACT]', 'V':'[ACG]', 'N':'[ACGT]'}
	JASPAR_dict = {}
	with open(jaspar_matrices_file, 'r') as matrices:
		for matrix in motifs.parse(matrices, 'jaspar'):
			#motif = motifs.read(matrix, 'jaspar')
			motif_counts = matrix.counts	
			consensus = str(motif_counts.degenerate_consensus)
			consensus = consensus.replace('N','')
			motif_name = matrix.name
			for code in IUPAC_dict:
				consensus = consensus.replace(code, IUPAC_dict[code])
			JASPAR_dict[motif_name]=consensus
	return JASPAR_dict

def make_bed(VCBerry_df, slop_len=15):
	bed_frame = pd.DataFrame()
	bed_frame['chrom'] = VCBerry_df['CHROM']
	bed_frame['start'] = VCBerry_df['POS'] - slop_len 
	bed_frame['stop'] = VCBerry_df['POS'] + slop_len
	bed_frame['CHROM_POS'] = VCBerry_df['CHROM_POS']
	bed = pybedtools.BedTool.from_dataframe(bed_frame)
	return bed

def get_fasta(VCBerry_df, bed, ref_fa):
	Jackfruit_bed = bed.sequence(fi=ref_fa)
	fasta_str = open(Jackfruit_bed.seqfn).read()
	fasta_list = fasta_str.split('\n')[:-1]
	fasta_dict = {}
	i=0
	for line in fasta_list:
		if line.startswith('>'):
			header = VCBerry_df.iloc[i]['CHROM_POS']
			i += 1
		else:
			fasta_dict[header] = line.upper()
	return fasta_dict

def motif_search(sequence, JASPAR_dict):
	motifs_set = set()
	for motif in JASPAR_dict:
		if re.search(JASPAR_dict[motif], sequence):
			motifs_set.add(motif)
	return motifs_set

def seq_disruptor(fasta_dict, VCBerry_df, JASPAR_dict, slop_len=15):
	find_replace_dict = {}
	for item in fasta_dict:
		df_slice = VCBerry_df.loc[VCBerry_df['CHROM_POS'] == item]
		ref = df_slice.iloc[0]['REF']
		alt = df_slice.iloc[0]['ALT']
		ref_seq = fasta_dict[item]
		ref_motifs = motif_search(ref_seq, JASPAR_dict)
		if ',' in alt:
			alt_list = alt.split(',')
			for var in alt_list:
				header = item + '_' + ref + '>' + var
				find_replace_dict[header] = {}
				#print(f'Expected_ref: {ref} | Inserted_alt: {alt}') 
				#print(fasta_dict[item][:slop_len-1]+ var+fasta_dict[item][slop_len:] )
				#print(fasta_dict[item])
				alt_seq = fasta_dict[item][:slop_len-1]+ var +fasta_dict[item][slop_len:]
				find_replace_dict[header]['ref'] = ref_seq
				find_replace_dict[header]['alt'] = alt_seq
				alt_motifs = motif_search(alt_seq, JASPAR_dict)
				disrupted_motifs = ref_motifs - alt_motifs
				gained_motifs = alt_motifs - ref_motifs
				find_replace_dict[header]['disrupted_motifs'] = disrupted_motifs
				find_replace_dict[header]['gained_motifs'] = gained_motifs
		else:
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
	return find_replace_dict

# I've downloaded some jaspar pfm files, and can read them with motifs
def main():
	file = sys.argv[1]
	vcf_file = sys.argv[2]
	slop_len = int(sys.argv[4])
	JASPAR_dict = parse_JASPAR(file)
	Jackfruit = VCBerry(vcf_file)
	Jackfruit_bed = make_bed(Jackfruit.snps)
	#print(Jackfruit_bed)
	Hg38 = pybedtools.example_filename(sys.argv[3])
	fasta_dict = get_fasta(Jackfruit.snps, Jackfruit_bed, Hg38)
	#print(fasta_dict)
	#print(JASPAR_dict)
	find_replace_dict = seq_disruptor(fasta_dict, Jackfruit.snps, JASPAR_dict, slop_len)
	for snp in find_replace_dict:
		print(snp)
		print(f'Reference sequence: {find_replace_dict[snp]["ref"]}')
		print(f'Alternate sequence: {find_replace_dict[snp]["alt"]}')
		print(f'Disrupted Motifs: {find_replace_dict[snp]["disrupted_motifs"]}')
		print(f'Gained Motifs: {find_replace_dict[snp]["gained_motifs"]}')
		print('\n')

if __name__ == '__main__':
	main()


