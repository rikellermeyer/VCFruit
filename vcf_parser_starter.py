#!/usr/bin/env python3


import sys
import pandas as pd


vcf_file = sys.argv[1]

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
		self.fruits = table
		
		# define function to split fruits table to snps and indels self objects

	################################
	##Potential function for later##
	################################
	# define function to write vcf from any pandas shaped attribute
	# def parse_info(self):
		# Parse self.header
			# regex INFO=<ID=(\w+)
			# store group 1 in list
		#raw_info = self.fruits.iloc[:,-1:]
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

raspberry = vcBerry(vcf_file)

print(raspberry.fruits)






