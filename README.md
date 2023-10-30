# VCFruit

## VCFruit.py makes a VCBerry Class Object
- Pulls in vcf file and makes a class called `VCBerry`.
- VCBerry generates the following pandas DataFrames:
  - `VCBerry.snps` are only SNPs.
  - `VCBerry.indels` are only INDELs.
  - `VCBerry.monomeric` are invariant sites.
- Call on VCBerry in a module via:
  - `new_df = VCBerry(vcfile)`
  - `function_return = new_df.snps`
- Other attributes of a VCBerry object:
  - `VCBerry.allvars` outputs a combined snp/indel DataFrame.
  - `VCBerry.header` provides the original vcf header for compiling a new vcf.

# Modules 
## Papaya.ipynb : Variant Position Visualization
- Papaya is a Jupyter notebook that visualizes the position of varaints on a chromosome.
- The frequency of variants at binned positions along the chromosome is visualized with a Manhattan plot and a heat map.
- Strawberry also plots the nucleotide change frequencies across all variants.

## Jackfruit.py : A Motif Module
- Jackfruit uses the JASPAR databse to identify variants within transcription factor binding sites.
- Jackfruit takes in a VCBerry.snp database and outputs a dictionary of reference and alternate TF binding motifs.
- The INDEL version of Jackfruit is in progress, named `Durian.py`
- ** Ideal output would be a .tsv

## Strawberry.py : Population-level Variant Analysis
- Strawberry extracts the genotype of every individual for every variant.
- Strawberry then calculates the ***

## Melon.py
- Annotates variants with the reference annotation.

## Grapes.py
- Grapes provides variant position in a chromosome. 

## WaterMelon.py: Variant Annotation
- WaterMelon annotates variants with the reference annotated genome.

## Lychee
### LycheeMelon.py
- LycheeMelon outputs reference and alternate sequence.  

### Lychee.py : Variant Effect Predictor
- Lychee takes the annotated reference and alternate sequences and predicts the effect of the variant.
- Lychee maps codons to amino acids and determines synonymous versus nonsynonymous mutations based on amino acid properties. 
- Lychee outputs the translated sequences and associated properties of the variants. **txt file?

# Fruit_Basket.py
- Fruit Basket integrates all the VCFruit modules with the exception of Papaya.
- The output is a series of files that describe, analyze, and annotate a contributed VCF. 
