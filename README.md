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

This script computes the minimum, maximum and center vectors for a selection, increase it according to your needs and convers the values from a spacing of 1A to a spacing of 0.375A. 

Use this script in VMD's Tk Console. 

After sourcing the script/pasting the process in the Tk Console, you can use it as such:

```get_cell moleculeID increment selection```

For example:

```get_cell 0 2 "resid 22 or resid 23"```

The result looks like this: 
```
This is the standard box for the specified contacts: 

20.489002227783203 12.73699951171875 25.845000743865967 

This is the center of the box: 

60.25102996826172 61.29500961303711 15.377567291259766 

You increased the box by 0. The new coordinates are: 

20.489002227783203 12.73699951171875 25.845000743865967 

Input for Autodock4 grid reference file (1A to 0.375A conversion): 

npts 55 34 69
spacing 0.375
gridcenter 60.25 61.3 15.38
```
