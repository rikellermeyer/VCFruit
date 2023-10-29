#!/usr/bin/env python3

import pandas as pd

# print option to 400 width
pd.set_option("display.width", 200)
# print all columns
pd.set_option("display.max_columns", 100)

def read_vcf(vcf_file):
    df = pd.read_csv(vcf_file, sep="\t", comment="#", header=None, names=["CHROM", "POS", "ID", "REF", "ALT", "QUAL", "FILTER", "INFO", "FORMAT", "NA00001", "NA00002", "NA00003"])

    # for line in df.INFO:
    #     print(line)

    # extract from INFO column the pattern [01.]+/[01.]+ and put it in a new column
    df["GT"] = df.INFO.str.extract(r"([01.]+/[01.]+)", expand=False)
    # print(df.GT)

    # pandas count unique values
    # print(df.GT.value_counts())

    # print(df.REF)
    # take dataframe df and create smller groups based on GT. Then count the number of each REF value within each group
    print(df.groupby("GT")["REF"].value_counts())
    print(df.groupby("GT")[["REF", "ALT"]].value_counts())

    d_ref = ...
    d_alt = ...
    d_gt = ...
    df_ref["n"] = df_GT["n"] + df_REF["n"] + df_ALT["n"]
    

if __name__ == "__main__":
    read_vcf("all_variants_1chr.vcf")
