#!/usr/bin/env python3

import os
import sys
import re
import pandas as pd
import numpy as np

class VCBerry(object):
	def __init__(self,vcf_file):
		# make this more specific to individual inputs
		
		with open(vcf_file, 'r') as file:
			table = pd.read_csv(vcf_file, sep='\t', comment='#')
			#iterate over comment lines and store header
			file_it = iter(file)
			header = ''
			for line in file_it:
				if line.startswith('##'):
					header += line
				elif line.startswith('#'):
					header += line
					raw_colnames = line[1:].rstrip()
					colnames = raw_colnames.split('\t')
					break
			self.header = header
		table.columns = colnames
		table['CHROM_POS'] = table.iloc[:,0] + '_' + table.iloc[:,1].astype(str)
		self.allvars = table
		snps_table = self.allvars.loc[(self.allvars['REF'].str.len()) == (self.allvars['ALT'].str.findall(r'^(\w+)').str.len())]
		indels_table = table.loc[(self.allvars['REF'].str.len()) != (self.allvars['ALT'].str.findall(r'^(\w+)').str.len())]
		
		self.snps = snps_table
		self.indels = indels_table


		# define function to split allvars table to snps and indels self objects

#df = pd.read_csv(vcf_file, sep="\t", comment="#", header=None, names=["CHROM", "POS",   "ID", "REF", "ALT", "QUAL", "FILTER", "INFO", "FORMAT", "C1", "C1_Rnd3", "C2", "C2_Rnd3", "  C3", "C3_Rnd2", "C3_Rnd3", "C4", "C4_Rnd2", "C4_Rnd3", "C5", "C5_Rnd2", "C5_Rnd3", "C6", "C  6_Rnd2", "C6_Rnd3", "C7", "C7_Rnd2", "C7_Rnd3", "E1", "E2", "E3", "E4", "E5", "E6", "E7", "  E8", "E8_Rnd2", "E9_Rnd2", "S1", "S2", "S3", "Sr1", "Sr2", "Sr3"])

def main():
  vcf_file = sys.argv[1]
  raspberry = VCBerry(vcf_file)
    #raspberry_snp_count = change_frequency(raspberry.snps)
# print(raspberry.snps[['CHROM','POS']])	#print(raspberry.allvars)
# print(raspberry.snps[['CHROM_POS','Sr2']])    #print(raspberry.allvars)
  print(raspberry.snps[["CHROM","POS","C1","C1_Rnd3","C2","C2_Rnd3","C3","C3_Rnd2","C3_Rnd3","C4","C4_Rnd2","C4_Rnd3","C5","C5_Rnd2","C5_Rnd3","C6","C6_Rnd2","C6_Rnd3","C7","C7_Rnd2","C7_Rnd3","E1","E2","E3","E4","E5","E6","E7","E8","E8_Rnd2","E9_Rnd2","S1","S2","S3","Sr1","Sr2","Sr3"]])

	#print('\n')
# print(raspberry.indels)
# print('\n')
# print(raspberry.snps)
  print('\n')
#	print(raspberry_snp_count)
#	print(raspberry.header)

if __name__ == '__main__':
	main()

