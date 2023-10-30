# VCFruit

## VCBerry Class Object
LVB: I added a class object called VCBerry to process vcf inputs.
Load it into your code with your import statements:
```
from VCBerry import *
```
To create the object simply call:
```
kiwi = VCBerry(vcf_file)
```

Your object will have the following attributes:
* allvars: A pd-style table with all your vcf information, and an additional column chrom_pos to be used as an identifier across subset items
* header: your original vcf header information, stored for later use
* snps: a subset table from allvars containing only single nucleotide polymorphism variants (where len(ref) = len(var))
* indels: a subset table from allvars containing only insert and deletion variants (where len(ref) != len(var))

This class object also contains the function:
```
kiwi_snps_counts = change_frequency(kiwi.snps)
```
This outputs a dictionary yielding counts for each possible SNP.


### Drupelets
Drupelets.py is a new python script which demonstrates plotting of the output of the change_frequency() function.\n
It uses matplotlib.pyplot to make a basic bar plot. \n
With the latest update, it now functions as a script that takes command line input, or can be imported as a module to a script. \n

Call it:
```
plot_snps_freq(kiwi_snps_counts, 'outputfile.png')
```
