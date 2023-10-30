#!/usr/bin/env python3
import sys

gff_file = open(sys.argv[1], 'r')
##saving and creating the header
header = ''


for line_h in gff_file:
    if line_h.startswith('##sequence-region NC_064409.1 1 78662058'):
       break
    if line_h.startswith('#'):
       header += line_h
       
print(header)
##adding the body with the first chromosome
gff_file = open(sys.argv[1], 'r')
for line_b in gff_file:
   if line_b.startswith('NC_064408.1'):
      print(line_b)
