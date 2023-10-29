#!/usr/bin/env python3
import re

test_string = 'ATGTTTTTCTTATCTCAGGAGCAATGGGGAAATGTTACCAGGTCCGAACTTATTGAGGTAAGACAGATTTAA'
#translate string:
for i in test_string:
	if i == 'T':
		transcript = test_string.replace('T', 'U')

#create a list of codons for each open reading frame:
codons_list = []
for index in range(0, len(transcript), 3):
	codon = transcript[index:index+3]
	codons_list.append(codon)	

#transcribe refrence and split into codons
ref_seq = 'TGTTTCTTCTTGTCTCAGGAGCAATGGGGAAATGTTACCAGGTCCGAACTTATTGAGGTAAGACAGATATAA'
for i in ref_seq:
	if i == 'T':
		ref_transcript = ref_seq.replace('T', 'U')

ref_codons_list = []
for index in range(0, len(ref_transcript), 3):
	ref_codon = ref_transcript[index:index+3]
	ref_codons_list.append(ref_codon)

#dictionary of amino acids and their codons:
amino_dict = {'Met':'AUG','Phe':['UUU', 'UUC'], 'Leu':['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'], 'Ile':['AUU', 'AUC', 'AUA'], 'Val':['GUU', 'GUC', 'GUA', 'GUG'], 'Ser':['UCU', 'UCC', 'UCA', 'UCG','AGU','AGC'], 'Pro':['CCU', 'CCC', 'CCA', 'CCG'], 'Thr':['ACU', 'ACC', 'ACA', 'ACG'], 'Ala':['GCU', 'GCC', 'GCA', 'GCG'], 'Tyr':['UAU', 'UAC'], 'His':['CAU', 'CAC'], 'Gln':['CAA','CAG'], 'Asn':['AAU', 'AAC'], 'Lys':['AAA', 'AAG'], 'Asp':['GAU', 'GAC'], 'Glu':['GAA','GAG'], 'Cys':['UGU','UGC'], 'Trp':'UGG', 'Arg':['CGU', 'CGC', 'CGA', 'CGG','AGA', 'AGG'], 'Gly':['GGU','GGC','GGA','GGG'],'STOP':['UAA', 'UAG', 'UGA']}  

ref_translated_sequence = []
translated_sequence = []
#translate both sequences:
for ref_codon in ref_codons_list:
	for amino_acid, ref_codon_list in amino_dict.items():
		if ref_codon in ref_codon_list:
			ref_translated_sequence.append(amino_acid)

for codon in codons_list:
	for amino_acid, codon_list in amino_dict.items():
		if codon in codon_list:
			translated_sequence.append(amino_acid)

#compare two protein sequences:
mutations_dict = {}
for index_1, amino_1 in enumerate(ref_translated_sequence):
	for index_2, amino_2 in enumerate(translated_sequence):
		if (amino_1 != amino_2) and (index_1 == index_2):
			mutations_dict[amino_1] = amino_2
			print(f"Found a nonsynonomous mutation at index {index_1+1}")
print(mutations_dict)


#mutation_severity - change in properties:
amino_info_dict = {
    'Arg': 'Positive', 'His': 'Positive', 'Lys': 'Positive',
    'Asp': 'Negative', 'Glu': 'Negative',
    'Ser': 'Polar_Uncharged', 'Thr': 'Polar_Uncharged', 'Asn': 'Polar_Uncharged', 'Gln': 'Polar_Uncharged',
    'Cys': 'Special_cases', 'Gly': 'Special_cases', 'Pro': 'Special_cases',
    'Ala': 'Hydrophobic', 'Val': 'Hydrophobic', 'Ile': 'Hydrophobic', 'Leu': 'Hydrophobic',
    'Met': 'Hydrophobic', 'Phe': 'Hydrophobic', 'Tyr': 'Hydrophobic', 'Trp': 'Hydrophobic'
}

for amino_ref, amino_var in mutations_dict.items():
	property_ref = amino_info_dict.get(amino_ref)
	property_var = amino_info_dict.get(amino_var)
	if property_ref != property_var:
		print(f"A change happened in amino acid property from {property_ref} to {property_var}")
	else:
		 print(f"No change in property {property_ref}")










