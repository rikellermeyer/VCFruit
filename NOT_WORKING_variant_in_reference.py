#!/usr/bin/env python3
import sys
import re
#opening the reference
ref_fna = open(sys.argv[1], 'r')
nt_count = 0
line_count = -1
pos = int(sys.argv[2])
for line in ref_fna:
  line_count += 1
  if line.startswith('>'): #skipping the header
    continue
  else:
    line = line.replace('\n', '')
    for nt in line:
       print(line)
       print(line_count)
       nt_count +=1
break
    #   if nt_count == int(sys.argv[2]):
     #     pos = pos - (line_count*80)
      #    print(pos)
     #     line_sub = re.sub(f'(.{{{pos}}})(.)(.+)', r'\1^\3', line)
      #    print('',line,'\n',line_sub) 
       
