#!/usr/bin/env python3
import re
import pandas as pd

test_string = 'ATGTTTTTCTTATCTCAGGAGCAATGGGGAAATGTTACCAGGTCCGAACTTATTGAGGTAAGACAGATTTAA'
#transcribe string:
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

ref_cod = []
var_cod = []
for i_1, cod_1 in enumerate(ref_codons_list):
	for i_2, cod_2 in enumerate(codons_list):
		if (cod_1 != cod_2) and (i_1 == i_2):
			ref_cod.append(cod_1)
			var_cod.append(cod_2)
print(ref_cod)
print(var_cod)

#dictionary of amino acids and their codons:
amino_dict = {'AUG':'Met',
							'UUU':'Phe', 'UUC':'Phe', 
							'UUA':'Leu', 'UUG':'Leu', 'CUU':'Leu', 'CUC':'Leu', 'CUA':'Leu', 'CUG':'Leu',
							'AUU':'Ile', 'AUC':'Ile', 'AUA':'Ile',
							'GUU':'Val', 'GUC':'Val', 'GUA':'Val', 'GUG':'Val',
							'UCU':'Ser', 'UCC':'Ser', 'UCA':'Ser', 'UCG':'Ser', 'AGU':'Ser', 'AGC':'Ser',
							'CCU':'Pro', 'CCC':'Pro', 'CCA':'Pro', 'CCG':'Pro',
							'ACU':'Thr', 'ACC':'Thr', 'ACA':'Thr', 'ACG':'Thr',
							'GCU':'Ala', 'GCC':'Ala', 'GCA':'Ala', 'GCG':'Ala',
							'UAU':'Tyr', 'UAC':'Tyr',
							'CAU':'His', 'CAC':'His',
							'CAA':'Gln', 'CAG':'Gln',
							'AAU':'Asn', 'AAC':'Asn',
							'AAA':'Lys', 'AAG':'Lys',
							'GAU':'Asp', 'GAC':'Asp',
							'GAA':'Glu', 'GAG':'Glu',
							'UGU':'Cys', 'UGC':'Cys',
							'UGG':'Trp',
							'CGU':'Arg','CGG':'Arg', 'AGA':'Arg', 'AGG':'Arg',
							'GGU':'Gly', 'GGC':'Gly', 'GGA':'Gly', 'GGG':'Gly',
							'UAA':'STOP', 'UAG':'STOP', 'UGA':'STOP'
}
						

ref_translated_sequence = []
translated_sequence = []
#translate both sequences:
amino_acid = {}
for ref_codon in ref_cod:
		if ref_codon in amino_dict:
			ref_translated_sequence.append(amino_dict[ref_codon])

for var_codon in var_cod:
		if var_codon in amino_dict:
			translated_sequence.append(amino_dict[var_codon])
print(ref_translated_sequence)
print(translated_sequence)

#compare two protein sequences:
syn_v_non = []

mutations_dict = {}
for index_1, amino_1 in enumerate(ref_translated_sequence):
	for index_2, amino_2 in enumerate(translated_sequence):
		if (amino_1 != amino_2) and (index_1 == index_2):
			syn_v_non.append('Non Syn')
			mutations_dict[amino_1] = amino_2
		elif (amino_1 == amino_2) and (index_1 == index_2):
			syn_v_non.append('Syn')
			mutations_dict[amino_1] = amino_2
print(syn_v_non)

#mutation_severity - change in properties:
amino_info_dict = {
    'Arg': 'Positive', 'His': 'Positive', 'Lys': 'Positive',
    'Asp': 'Negative', 'Glu': 'Negative',
    'Ser': 'Polar_Uncharged', 'Thr': 'Polar_Uncharged', 'Asn': 'Polar_Uncharged', 'Gln': 'Polar_Uncharged',
    'Cys': 'Special_cases', 'Gly': 'Special_cases', 'Pro': 'Special_cases',
    'Ala': 'Hydrophobic', 'Val': 'Hydrophobic', 'Ile': 'Hydrophobic', 'Leu': 'Hydrophobic',
    'Met': 'Hydrophobic', 'Phe': 'Hydrophobic', 'Tyr': 'Hydrophobic', 'Trp': 'Hydrophobic'
}

change_in_quality = [] 
for amino_ref, amino_var in mutations_dict.items():
	quality_ref = amino_info_dict.get(amino_ref)
	quality_var = amino_info_dict.get(amino_var)
	if quality_ref != quality_var:
		change_in_quality.append(f"{quality_ref} to {quality_var}")
	else:
		 change_in_quality.append("-")

data =[]
for ref, var, ref_amino, var_amino, syn_vs_non, change_quality in zip(ref_cod, var_cod, ref_translated_sequence, translated_sequence, syn_v_non, change_in_quality):
	data.append({
		'ref':ref, 
		'var':var,
		'ref_amino':ref_amino,
		'var_amino':var_amino,
		'Syn_vs_nonSyn':syn_vs_non,
		'Change_in_quality':change_quality
})
df = pd.DataFrame(data)
#Ka/Ks calculation:
#Ratio of mutations that change a specific protein structure to mutations that do not change specific protein. This ratio is used to estimate the selection pressure a given protein or section of DNA experiences. 


print(df)






