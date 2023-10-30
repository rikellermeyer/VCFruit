#!/usr/bin/env python3
import sys
import pandas as pd
from VCBerry import *

###beginning with the annotations
def annotation(snp_table):
 gff_file = open(sys.argv[2], 'r') #taking the gff file
 gff_head = ['chrom_id', 'Source', 'F_type', 'F_start', 'F_end', 'Score', 'Strand', 'Phase', 'Attributes']
 gff_table = pd.read_csv(gff_file, sep = '\t', comment = '#', names = gff_head) #table in panda
 for index_vcf, row_vcf in snp_table.iterrows():
    for index_gff, row_gff in gff_table.iterrows():
        if row_vcf['CHROM'] == row_gff['chrom_id']:
           if int(row_gff['F_start']) < int(row_vcf['POS']) < int(row_gff['F_end']): #It works!!! Found the position of the vcf inside the gff
                print(row_gff['chrom_id'],'\t',row_gff['F_type'],'\t',row_gff['F_start'],'\t',row_gff['F_end'],'\t',row_gff['Attributes'],'\t',row_vcf['POS'],'\t',row_vcf['ID'],'\t',row_vcf['REF'],'\t',row_vcf['ALT'],'\t',row_vcf['INFO']) 
 return()            

if __name__=='__main__':
  vcberry = VCBerry(sys.argv[1]) #input the vcf
  snp_table = vcberry.snps
  annotation(snp_table)           
