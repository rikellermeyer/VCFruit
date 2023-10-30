#!/usr/bin/env python3
import sys
import pandas as pd
def melon_tab(melon_out):

 header = ['chrom_id','F_type','F_start','F_end','Attributes','POS','ID','REF','ALT','INFO']
 out_file = open(sys.argv[1], 'r')
 out_table = pd.read_csv(out_file, sep = '\t', names = header)
 print(out_table)
 return()

if __name__ == '__main__':

 melon_tab(sys.argv[1])

