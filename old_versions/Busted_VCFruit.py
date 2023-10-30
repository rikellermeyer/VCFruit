#!/usr/bin/env python3

#Non-fruit dependencies
import os
import sys
import re
import pandas as pd


#################
##VCBerry Class##
#################

class VCBerry(object):
        def __init__(self,vcf_file):
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
                                        colnames = raw_colnames.split('\t') # stores last header to be column
                                        break
                        self.header = header # It's an attribute now
                table.columns = colnames
								# because snp IDs are not universal, create key for identifying snps
                table['CHROM_POS'] = table.iloc[:,0] + '_' + table.iloc[:,1].astype(str) 
                self.allvars = table # all variants attribute
                snps_table1 = self.allvars.loc[(self.allvars['ALT'].str.findall(r'^(\w)+').str.len() == 1)] # where ref is same len as var
                snps_table2 = self.allvars.loc[(self.allvars['REF'].str.len() == 1)]
                snps_table = pd.concat([snps_table1, snps_table2], axis=0, join='inner')
                indels_table1 = self.allvars.loc[(self.allvars['REF'].str.len() >= 2)]
                indels_table2 = self.allvars.loc[(self.allvars['ALT'].str.findall(r'^(\w)+').str.len() >= 2)] # where it is not
                indels_table = pd.concat([indels_table1, indels_table2], axis=0, join='outer')
                self.monomeric = self.allvars.loc[self.allvars['ALT'] == '*'] # store monomorphic
                self.snps = snps_table # make snps and indels as attributes
                self.indels = indels_table

def main():
        vcf_file = sys.argv[1]
        raspberry = VCBerry(vcf_file)
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
        #print(raspberry.header)
if __name__ == '__main__':
        main()
