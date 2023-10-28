#!/usr/bin/env python3

import sys
from vcf_parser_starter import *

file = sys.argv[1]

kiwi = vcBerry(file)
kiwi_snp_count = change_frequency(kiwi.snps)

print(kiwi_snp_count)

