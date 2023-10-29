#!/usr/bin/env python3

#This will be at least one function used for parsing the JASPAR database for degenerate consensus motifs
#and also for searching sequences for motifs
# I could include the functionality for iterating through variants and making the sequences
import sys
import re
from Bio import motifs
from VCBerry import *
import pybedtools

IUPAC_dict = {'R':'[AG]',
'Y':'[CT]',
'S':'[GC]',
'W':'[AT]',
'K':'[GT]',
'M':'[AC]',
'B':'[CGT]',
'D':'[AGT]',
'H':'[ACT]',
'V':'[ACG]',
'N':'[ACGT]'}
def make_bed(VCBerry_df, slop_len=15):
	bed_frame = pd.DataFrame()
	bed_frame['chrom'] = VCBerry_df['CHROM']
	bed_frame['start'] = VCBerry_df['POS'] - slop_len 
	bed_frame['stop'] = VCBerry_df['POS'] + slop_len
	bed_frame['CHROM_POS'] = VCBerry_df['CHROM_POS']
	bed = pybedtools.BedTool.from_dataframe(bed_frame)
	return bed

# I've downloaded some jaspar pfm files, and can read them with motifs
def main():
	file = sys.argv[1]
	vcf_file = sys.argv[2]
	JASPAR_dict = {}
	with open(file, 'r') as matrices:
		for matrix in motifs.parse(matrices, 'jaspar'):
			#motif = motifs.read(matrix, 'jaspar')
			motif_counts = matrix.counts	
			consensus = str(motif_counts.degenerate_consensus)
			consensus = consensus.replace('N','')
			motif_name = matrix.name
			for code in IUPAC_dict:
				consensus = consensus.replace(code, IUPAC_dict[code])
			raw_consensus = r'{}'.format(consensus)
			JASPAR_dict[motif_name]=raw_consensus
	Jackfruit = VCBerry(vcf_file)
	Jackfruit_bed = make_bed(Jackfruit.snps)
	print(Jackfruit_bed)
	Hg38 = pybedtools.example_filename(sys.argv[3])
	Jackfruit_bed = Jackfruit_bed.sequence(fi=Hg38)
	print(open(Jackfruit_bed.seqfn).read())
	#Jackfruit.snps['sequence'] = Jackfruit_bed.sequence(fi=Hg38)
	#print(Jackfruit.snps)

if __name__ == '__main__':
	main()


