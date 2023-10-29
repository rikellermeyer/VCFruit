#!/usr/bin/env python3

import sys
from vcf_parser_starter import *
import numpy as np
import matplotlib.pyplot as plt

file = sys.argv[1]

kiwi = vcBerry(file)
kiwi_snp_count = change_frequency(kiwi.snps)

print(kiwi_snp_count)
snp_types = list(kiwi_snp_count.keys())

plt.bar(range(len(kiwi_snp_count)), kiwi_snp_count.values(), tick_label=snp_types)
plt.xticks(rotation=45)
plt.ylabel('Count')
plt.xlabel('SNP Type')
plt.savefig('snp_counts.png')
