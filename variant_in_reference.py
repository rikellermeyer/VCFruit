#!/usr/bin/env python3
import sys
import re
from VCBerry import *


count_line = -1
vcberry = VCBerry(sys.argv[1])
snp_table = vcberry.snps
var_dict = variant_position(snp_table)
ref_fna = open(sys.argv[2], 'r')

print(var_dict)
for line in ref_fna:
   line = line.replace('\n', '')
   count_line += 1
   for pos in var_dict:
      pos_var_line = int(pos/80)
      pos_nt = pos%80
      if line.startswith('>'):
           continue
      else:
          if pos_var_line == count_line:
            regex = r"\1" + re.escape(var_dict[pos]) + r"\3"
            line_sub = re.sub(f'(.{{{pos_nt}}})(.)(.+)', regex, line)
            print('position:', pos, '\n',line,'\n',line_sub)
print('finish')
