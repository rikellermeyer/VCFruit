#!/usr/bin/env python3
import re
import pandas as pd
from VCBerry import *
# print option to 400 width
pd.set_option("display.width", 200)
# print all columns
pd.set_option("display.max_columns", 100)
#def read_vcf(vcf_file):

#ref_col = vcf_df['REF']
#print(vcf_df)

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

#df = pd.DataFrame(vcf_df)
#columns_to_exclude = ["ID", "QUAL", "FILTER", "INFO", "FORMAT", "CHROM_POS"]
#lines_to_extract = ["C1", "C1_Rnd3", "C2", "C2_Rnd3", "C3", "C3_Rnd2", "C3_Rnd3", "C4", "C4_Rnd2", "C4_Rnd3", "C5", "C5_Rnd2", "C5_Rnd3", "C6", "C6_Rnd2", "C6_Rnd3", "C7", "C7_Rnd2", "C7_Rnd3", "E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", "E8_Rnd2", "E9_Rnd2", "E10_Rnd2", "E11_Rnd2","E12_Rnd2", "E13_Rnd2", "E14_Rnd2", "E15_Rnd2", "E16_Rnd2", "E8_Rnd2", "S1", "S2", "S3", "Sr1", "Sr2", "Sr3"]
#for line in lines_to_extract:
#    vcf_df[line] = vcf_df[line].str[:3]
#     df[line] = df[line].str[:3]
#vcf_df = vcf_df.drop(columns=columns_to_exclude, errors='ignore')
#print(vcf_df)

#	vcf_df_filtered = []
#	i = 0 
#	with open Strawberry as file:
#			for column in file
#					if re.match(r"^[1.0]+$", column):
#							Strawberry.append(column.strip())
#	for columns in Strawberry
#	print(columns)

    #df = pd.read_csv(vcf_file, sep="\t", comment="#", header=None, names=["CHROM", "POS", "ID", "REF", "ALT", "QUAL", "FILTER", "INFO", "FORMAT", "C1", "C1_Rnd3", "C2", "C2_Rnd3", "C3", "C3_Rnd2", "C3_Rnd3", "C4", "C4_Rnd2", "C4_Rnd3", "C5", "C5_Rnd2", "C5_Rnd3", "C6", "C6_Rnd2", "C6_Rnd3", "C7", "C7_Rnd2", "C7_Rnd3", "E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", "E8_Rnd2", "E9_Rnd2", "S1", "S2", "S3", "Sr1", "Sr2", "Sr3"])

    # for line in df.INFO:
    #     print(line)

    # extract from INFO column the pattern [01.]+/[01.]+ and put it in a new column
#    df["GT"] = df.INFO.str.extract(r"([01.]+/[01.]+)", expand=False)
    # print(df.GT)
    # pandas count unique values
    # print(df.GT.value_counts())
    # print(df.REF)
    # take dataframe df and create smller groups based on GT. Then count the number of each REF value within each group
#    print(df.groupby("GT")["REF"].value_counts())
#    print(df.groupby("GT")[["REF", "ALT"]].value_counts())
#    d_ref = ...
#    d_alt = ...
#    d_gt = ...
#    df_ref["n"] = df_GT["n"] + df_REF["n"] + df_ALT["n"]
#if __name__ == "__main__":
#    read_vcf("all_variants_1chr.vcf")
