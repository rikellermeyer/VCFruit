#!/usr/bin/env python3
import re
import pandas as pd
from VCBerry import *
pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 100)
def GT_annotation(VCBerry_df):
	columns_to_exclude = ["ID", "QUAL", "FILTER", "INFO", "FORMAT", "CHROM_POS"]
	lines_to_extract = ["C1", "C1_Rnd3", "C2", "C2_Rnd3", "C3", "C3_Rnd2", "C3_Rnd3", "C4", "C4_Rnd2", "C4_Rnd3", "C5", "C5_Rnd2", "C5_Rnd3", "C6", "C6_Rnd2", "C6_Rnd3", "C7", "C7_Rnd2", "C7_Rnd3", "E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", "E8_Rnd2", "E9_Rnd2", "E10_Rnd2", "E11_Rnd2","E12_Rnd2", "E13_Rnd2", "E14_Rnd2", "E15_Rnd2", "E16_Rnd2", "E8_Rnd2", "S1", "S2", "S3", "Sr1", "Sr2", "Sr3"]
	for line in lines_to_extract:
		VCBerry_df[line] = VCBerry_df[line].str[:3]
	VCBerry_df = VCBerry_df.drop(columns=columns_to_exclude, errors='ignore')
	return VCBerry_df


def main():
	Strawberry = VCBerry("all_variants_1chr.vcf")
	vcf_df = Strawberry.allvars
	filtered_df = GT_annotation(vcf_df)
	print(filtered_df)

if __name__ == '__main__':
    main()

