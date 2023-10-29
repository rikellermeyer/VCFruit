#!/usr/bin/env python3

#This will be at least one function used for parsing the JASPAR database for degenerate consensus motifs
#and also for searching sequences for motifs
# I could include the functionality for iterating through variants and making the sequences
import sys
import re
from Bio import motifs

#alternatively....
# from Bio.motifs.jaspar.db import JASPAR5


#Potentially for the database...
# I've downloaded some jaspar pfm files, and can read them with motifs
file_list = sys.argv[1:]
for file in file_list: #put the pfm file path at the end, so update this as you add other inputs
	with open(file, 'r') as matrix:
		motif = motifs.read(matrix, 'jaspar')
		motif_counts = motif.counts	
		consensus = motif_counts.degenerate_consensus
		motif_name = motif.name
		print(motif_name)
		print(motif_counts)
		print(consensus, '\n\n')
		#print(motif)




