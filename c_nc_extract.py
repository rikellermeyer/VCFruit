#!/usr/bin/env python3

## According to tester_vcf lines, we can do the following to extract coding non coding gene variants but let's wait until we get the actual vcf files before making this
## import vcf
##  @@ -122,4 +122,40 @@ for record in vcf_reader:
##    print(f"Variant: {record.CHROM}:{record.POS}, Gene Info: {gene_info}, NSF: {nsf}, NSM: {nsm}, NSN: {nsn}, SYN: {syn}, U3: {u3}, U5: {u5}, ASS: {ass}, DSS: {dss}, INT: {intron}, R3: {r3}, R5: {r5}")



#We will use PyVCF library to parse the VCF file. 
import vcf

def extract_information_from_vcf(vcf_file):
    # Open the VCF file
    vcf_reader = vcf.Reader(open(vcf_file, 'r'))
    vcf_writer = vcf.Writer(open('output_annotated.vcf', 'w'), vcf_reader)
# ...
for record in vcf_reader:
    # Extract SNP information
    if record.is_snp:
        print("SNP - Chromosome: {}, Position: {}, Reference: {}, Alt: {}".format(
            record.CHROM, record.POS, record.REF, record.ALT))
            
    # Extract INDEL information
    if record.is_indel:
        print("INDEL - Chromosome: {}, Position: {}, Reference: {}, Alt: {}".format(
            record.CHROM, record.POS, record.REF, record.ALT))
            
    # Extract CNV information (assuming copy number is available in the INFO field)
    if 'CN' in record.INFO:
        print("CNV - Chromosome: {}, Position: {}, Copy Number: {}".format(
            record.CHROM, record.POS, record.INFO['CN']))
            
    vcf_writer.write_record(record)  # Corrected indentation
    
vcf_file_path = 'tester_vcf.vcf'  # Corrected indentation
# ...













#
#    for record in vcf_reader:
        # Extract SNP information
#        if record.is_snp:
#            print("SNP - Chromosome: {}, Position: {}, Reference: {}, Alt: {}".format(
#                record.CHROM, record.POS, record.REF, record.ALT))

        # Extract INDEL information
#        if record.is_indel:
#            print("INDEL - Chromosome: {}, Position: {}, Reference: {}, Alt: {}".format(
#                record.CHROM, record.POS, record.REF, record.ALT))
        # Extract CNV information (assuming copy number is available in the INFO field)
#        if 'CN' in record.INFO:
#           print("CNV - Chromosome: {}, Position: {}, Copy Number: {}".format(
#                record.CHROM, record.POS, record.INFO['CN']))
#vcf_writer.write_record(record)
#vcf_file_path = 'tester_vcf.vcf'








# ...
for record in vcf_reader:
    # Extract SNP information
    if record.is_snp:
        print("SNP - Chromosome: {}, Position: {}, Reference: {}, Alt: {}".format(
            record.CHROM, record.POS, record.REF, record.ALT))

    # Extract INDEL information
    if record.is_indel:
        print("INDEL - Chromosome: {}, Position: {}, Reference: {}, Alt: {}".format(
            record.CHROM, record.POS, record.REF, record.ALT))

    # Extract CNV information (assuming copy number is available in the INFO field)
    if 'CN' in record.INFO:
        print("CNV - Chromosome: {}, Position: {}, Copy Number: {}".format(
            record.CHROM, record.POS, record.INFO['CN']))

    vcf_writer.write_record(record)  # Corrected indentation

vcf_file_path = 'tester_vcf.vcf'  # Corrected indentation
# ...

