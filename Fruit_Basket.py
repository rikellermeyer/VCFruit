#!/usr/bin/env python3

from VCFruit import *

vcf_file = sys.argv[1]




print('Making VCBerry Object')
Fruit_Basket = VCBerry(vcf_file)
all_attributes = dir(Fruit_Basket)
print('Attributes of Fruit_Basket:')
for attribute in all_attributes:
	if attribute.startswith('__'):
		continue
	else:
		print(f'\t{attribute}')
print('\n\n')

print('Testing Grapes function change_frequency()')
test_dict = change_frequency(Fruit_Basket.snps)
print('SNP Change Frequencies Dictionary:')
print(test_dict)

print('Testing Grapes function variant_position()')
sm_dict = variant_position(Fruit_Basket.allvars)
print('Positions of Variants in Fruit_Basket:')
for key in sm_dict:
	print(str(key)+'\t'+ sm_dict[key])
