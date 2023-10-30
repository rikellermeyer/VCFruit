#!/usr/bin/env python3
import sys
import re
from VCBerry import *


def var_in_ref(var_dict):
 for pos in var_dict:  ###FOR EACH VARIANT
  pos_var_line = int(pos/80)  #calculating the line. int will round the float always lower, so the first line will be number 0. a line is of 80 nts
  pos_nt = pos%80 #need this to calculate the position in each line of the fasta. A line is of 80 nts, so the reminder will be the position in the single line
  count_line = -1 #line number is -1 because first line will be number 0 #resetting it each time it founds a variant
  ref_fna = open(sys.argv[2], 'r') #input the reference
  for line in ref_fna:  ###LOOK IN EACH LINE OF THE FASTA REF 
      line = line.replace('\n', '')
      count_line += 1  #line counter
      if line.startswith('>'): #skipping the header
           continue
      else:
          if pos_var_line == count_line:  ###IF YOU ARE IN THE LINE OF THE VARIANT, HIGHLIGHT IT
            regex = r"\1^" + re.escape(var_dict[pos]) + r"^\3"  #creating the regular expression to substitute
            line_sub = re.sub(f'(.{{{pos_nt}}})(.)(.+)', regex, line)
            print('position:', pos, '\n',line,'\n',line_sub)
 return()  
if __name__=='__main__':
 vcberry = VCBerry(sys.argv[1]) #input the vcf
 snp_table = vcberry.snps
 var_dict = variant_position(snp_table)
 var_in_ref(var_dict)
