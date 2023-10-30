#!/usr/bin/env python3

import os
import sys
import pandas as pd
from pyarrow import csv
def skip_comment(row):
	if row.text.startswith('#'):
		return 'skip'
	else:
		return 'error'
 
class vcBerry(object):
	def __init__(self,vcf_file):
    # make this more specific to individual inputs
 
    #with open(vcf_file, 'r') as file:
      #table = pd.read_csv(vcf_file, sep='\t', comment='#')
		table = csv.read_csv(vcf_file, parse_options=csv.ParseOptions(delimiter='\t', invalid_row_handler=skip_comment)) 
      #iterate over comment lines and store header
		with open(vcf_file, 'r') as file:
			header = ''
			for line in file:
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


def main():
	input_vcf = sys.argv[1]
	strawb = vcBerry(input_vcf)
	print(strawb.allvars)

if __name__ == '__main__':
	main()
