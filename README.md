# Automatization Toolkit
This repository contains scripts I've written that help me parse various file formats. 

# Count residues from single/multiple-sequence FASTA file.
You can use this script to:
- count the total number of residues in a single-sequence/multiple-sequence FASTA file;
- count the total number of each residue per sequence;
- sum the total number of residue X in a multiple-sequence FASTA file and average it. 

The output is a CSV file. 
To run this script: 

```python countFastaAminoAcid.py folderpath```

For example, for the current folder:

``` python countFastaAminoAcid.py .```
