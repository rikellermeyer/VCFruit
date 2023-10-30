#!/usr/bin/env python3

#Non-fruit dependencies
import os
import sys
import re
import pandas as pd
import numpy as np
from Bio import motifs
import pybedtools
import matplotlib.pyplot as plt

###################
## VCBerry Class ##
###################
from VCFruit import *

###################
##    Fruits     ##
###################
from Strawberry import *
from Grapes import *
from Drupelets import *
from Jackfruit import *
from Melon import *
from Panda_Melon import *
from Lychee import *
from WaterMelon import *



def main_main():
	file = sys.argv[1]
	vcf_file = sys.argv[2]
	ref_fa = sys.argv[3]
	slop_len = sys.argv[4]
	print(f'Running Jackfruit on {vcf_file})')
	Jackfruit.main(file, vcf_file, ref_fa, slop_len)
	print(f'Running Drupelets on {vcf_file})')
	Drupelets.main(vcf_file)
	print(f'Running Grapes on {vcf_file})')
	Grapes.main(vcf_file)
	print(f'Running Strawberry')
	Strawberry.main()
	print(f'Running Panda_Melon on {vcf_file})')
	Panda_Melon.melon_tab(vcf_file)
	print(f'Running Lychee on {vcf_file})')
	Lychee.find_syn_v_non_syn(vcf_file, 'r')
	print(f'Running WaterMelon on {vcf_file})')
	WaterMelon.var_in_ref(vcf_file)
	

if __name__ = '__main__':
	main_main()
