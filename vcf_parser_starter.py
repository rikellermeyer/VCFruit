#!/usr/bin/env python3

import os
import sys
import pandas as pd



class vcBerry(object):
	def __init__(self,vcf_file):
		# make this more specific to individual inputs
		
		with open(vcf_file, 'r') as file:
			table = pd.read_csv(vcf_file, sep='\t', comment='#')
			#iterate over comment lines and store header
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
		snps_table = pd.DataFrame(columns=self.allvars.columns)
		indels_table = pd.DataFrame(columns=self.allvars.columns)
		for index, row in self.allvars.iterrows():
			ref = row[3]
			alt = row[4]
			if ',' in alt:
				alt_list = alt.split(',')
				if len(alt_list[0]) == len(ref):
					#snps_table = snps_table.append(row)
					snps_table = pd.concat([snps_table, row.to_frame().T], ignore_index=True)
				else:
					#indels_table = indels_table.append(row)
					indels_table = pd.concat([indels_table, row.to_frame().T], ignore_index=True)
			elif len(alt) == len(ref):
				#snps_table = snps_table.append(row)
				snps_table = pd.concat([snps_table, row.to_frame().T], ignore_index=True)
			else:
				#indels_table = indels_table.append(row)
				indels_table = pd.concat([indels_table, row.to_frame().T], ignore_index=True)
		self.snps = snps_table
		self.indels = indels_table
		# define function to split allvars table to snps and indels self objects

	################################
	##Potential function for later##
	################################
	# define function to write vcf from any pandas shaped attribute
	# def parse_info(self):
		# Parse self.header
			# regex INFO=<ID=(\w+)
			# store group 1 in list
		#raw_info = self.allvars.iloc[:,-1:]
		#return raw_info
		# convert raw_info into a list
		# make empty df with header_list as column IDs
		# for item in info_list:
			# make temp_list = []
			# split by ';'
			# make dictionary pairs using split on '='
			# for item in header_list
				# if item in dictionary:
					# get value for item
					# append to temp_list
				#else:
					# value = 'NA'
			# append temp_list to pandas df

def change_frequency(snps_table):
	counts_dict = {'A>T':0, 'A>C':0, 'A>G':0,
								'T>A':0, 'T>C':0, 'T>G':0,
								'C>A':0, 'C>T':0, 'C>G':0,
								'G>A':0, 'G>T':0, 'G>C':0}
	for index, row in snps_table.iterrows():
		ref = row[3]
		alt = row[4] 
		if ',' in alt:
			alt_list = alt.split(',')
			for nt in alt_list:
				snp_type = ref + '>' + nt
				counts_dict[snp_type] += 1
		else:
			snp_type = ref + '>' + alt
			counts_dict[snp_type] += 1
	return counts_dict

def main():
	vcf_file = sys.argv[1]
	raspberry = vcBerry(vcf_file)
	raspberry_snp_count = change_frequency(raspberry.snps)

	#print(raspberry.allvars)
	#print('\n')
	#print(raspberry.indels)
	#print('\n')
	print(raspberry.snps)
	print('\n')
	print(raspberry_snp_count)


if __name__ == '__main__':
	main()


