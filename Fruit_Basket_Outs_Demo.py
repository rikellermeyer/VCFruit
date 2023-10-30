#!/usr/bin/env python3

from Fruit_Basket import *

vcf_file = sys.argv[1]
JASPAR_file = sys.argv[2]
ref_fa = sys.argv[3]
slop_len = int(sys.argv[4])



print('Making VCBerry Object')
Fruit_Pie = VCBerry(vcf_file)
all_attributes = dir(Fruit_Pie)
print('Attributes of Fruit_Pie:')
for attribute in all_attributes:
	if attribute.startswith('__'):
		continue
	else:
		print(f'\t{attribute}')
print('\n\n')

print('Testing Grapes function change_frequency()')
test_dict = change_frequency(Fruit_Pie.snps)
print('SNP Change Frequencies Dictionary:')
print(test_dict)
print('\n\n')

print('Testing Grapes function variant_position()')
sm_dict = variant_position(Fruit_Pie.allvars)
print('Positions of Variants in Fruit_Pie:')
for key in sm_dict:
	print(str(key)+'\t'+ sm_dict[key])
print('\n\n')

print('Testing Jackfruit functions')
print('Make Bed and Get Sequences:')
Jackfruit_bed = make_bed(Fruit_Pie.snps)
Ref_fasta = pybedtools.example_filename(ref_fa)
fasta_dict = get_fasta(Fruit_Pie.snps, Jackfruit_bed, Ref_fasta)
for seq in fasta_dict:
	print(f'Position: {seq}')
	print(f'Sequence: {fasta_dict[seq]}')
print('\n')
print('Disrupting sequenceswith extension size {slop_len} and getting motif changes:')
JASPAR_dict = parse_JASPAR(JASPAR_file)
find_replace_dict = seq_disruptor(fasta_dict, Fruit_Pie.snps, JASPAR_dict, slop_len)
for snp in find_replace_dict: # print dictionary all pretty
	print(f'SNP Info:{snp}')
	print(f'Reference sequence: {find_replace_dict[snp]["ref"]}')
	print(f'Alternate sequence: {find_replace_dict[snp]["alt"]}')
	print(f'Disrupted Motifs: {find_replace_dict[snp]["disrupted_motifs"]}')
	print(f'Gained Motifs: {find_replace_dict[snp]["gained_motifs"]}')

print('\n\n')
