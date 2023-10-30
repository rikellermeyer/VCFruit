#!/usr/bin/env python3

#Non-fruit dependencies
import os
import sys
import re
import pandas as pd
import numpy as np
from Bio import motifs
import pybedtools


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
                snps_table = self.allvars.loc[(self.allvars['REF'].str.len()) == (self.allvars['ALT'].str.findall(r'^(\w+)').str.len())] # where ref is same len as var
                indels_table = table.loc[(self.allvars['REF'].str.len()) != (self.allvars['ALT'].str.findall(r'^(\w+)').str.len())] # where it is not
                only_indels_table = indels_table.loc[indels_table['ALT'] != '*'] # '*' indicates monomorphic
                self.monomeric = indels_table.loc[indels_table['ALT'] == '*'] # store monomorphic
                self.snps = snps_table # make snps and indels as attributes
                self.indels = only_indels_table
