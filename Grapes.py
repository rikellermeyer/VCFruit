#!/usr/bin/env python3

## Pulling out some small functions from VCBerry.py
from VCFruit import *
import pandas as pd
import sys

def change_frequency(snps_table):
	counts_dict = {'A>T':0, 'A>C':0, 'A>G':0, # Empty dictionary
								'T>A':0, 'T>C':0, 'T>G':0,
								'C>A':0, 'C>T':0, 'C>G':0,
								'G>A':0, 'G>T':0, 'G>C':0}
	for index, row in snps_table.iterrows(): #iterrows is a pandas workaround
		ref = row[3]
		alt = row[4] 
		if ',' in alt: # Again to deal with multi variant snps
			alt_list = alt.split(',')
			for nt in alt_list: # iterate through each
				snp_type = ref + '>' + nt # recreate dictionary keys
				if snp_type not in counts_dict:
					continue
				else:
					counts_dict[snp_type] += 1 # count
		else:
			snp_type = ref + '>' + alt # recreate dictionary keys
			if snp_type not in counts_dict:
				continue
			else:
				counts_dict[snp_type] += 1 # count
	return counts_dict


def variant_position(snps_table):
	var_pos = dict(zip(snps_table['POS'], snps_table['ALT'])) # pairs snp to chromosomal pos
	return var_pos


def main():
        vcf_file = sys.argv[1]
        raspberry = VCBerry(vcf_file)
        raspberry_snp_count = change_frequency(raspberry.snps)
        print(raspberry)
        #print(raspberry.allvars)
        #print('\n')
        print(raspberry.indels['REF'], raspberry.indels['ALT'])
        print(f'Number of indels: {len(raspberry.indels)}')
        #print('\n')
        print(raspberry.snps[['POS', 'ALT']])
        print('\n')
        #print(raspberry.monomeric)
        print('\n')
        #print(raspberry_snp_count)
        #print(raspberry.header)
        variation_dictionary = variant_position(raspberry.snps)
        print(variation_dictionary)
if __name__ == '__main__':
        main()
