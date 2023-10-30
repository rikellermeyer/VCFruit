#!/usr/bin/env python3

import sys
from VCFruit import *
import numpy as np
import matplotlib.pyplot as plt


def plot_snp_freq(dictionary, out_file):
	snp_types = list(dictionary.keys())
	plt.bar(range(len(dictionary)), dictionary.values(), tick_label=snp_types)
	plt.xticks(rotation=45)
	plt.ylabel('Count')
	plt.xlabel('SNP Type')
	plt.savefig(out_file)


def main():
	file = sys.argv[1]
	kiwi = VCBerry(file)
	kiwi_snp_count = change_frequency(kiwi.snps)
	print(kiwi_snp_count)
	plot_snp_freq(kiwi_snp_count, 'snp_counts.png')

if __name__ == '__main__':
	main()
