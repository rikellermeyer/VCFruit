#!/usr/bin/env python3

## Pulling out some small functions from VCBerry.py

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
				counts_dict[snp_type] += 1 # count
		else:
			snp_type = ref + '>' + alt # recreate dictionary keys
			counts_dict[snp_type] += 1 # count
	return counts_dict


def variant_position(snps_table):
	var_pos = dict(zip(snps_table['POS'], snps_table['ALT'])) # pairs snp to chromosomal pos
	return var_pos
