#!/usr/bin/env python3
import sys

ref_file = open(sys.argv[1], 'r')
##taking only the first chromosome
for line in ref_file:
   line = line.replace('\n', '')
   if line.startswith('>NC_064409.1'):
      break
   else:
      print(line)
   
