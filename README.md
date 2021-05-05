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

# Measure binding site and prepare reference file for Autodock4. 

This script computes the minimum, maximum and center vectors for a selection, increments it according to your needs and convers the values from a spacing of 1A to a spacing of 0.375A. 

Use this script in VMD's Tk Console. 

After sourcing the script/pasting the process in the Tk Console, you can use it as such:

```get_cell moleculeID increment selection```

For example:

```get_cell 0 2 "resid 22 or resid 23"```

