# NOE_Distance_Calculator
Uses a PDB file to calculate NOE distances within a desired distance for desired atoms

***program to run is NOE_GUI.py***

Upload your PDB file, indicate the boundaries of the sequence of your protein (numbering must match PDB numbering), and the PDB chain to search. 

Check what atoms of which amino acids you wish to search, and what is the cutoff for the distance you wish to see for an amino acid. 

Then simply type in an atom of an amino acid, and the program will find all atoms within the desired distance of your search. Format for search should be residue type, residue number, atom type.

***Make sure to click ENTER for all entries, or they will not be included***

E.G.

PDB File = 1mmi.pdb

Start = 1

End = 243

Chain = A

We only wish to see the methyl groups that are within 5A of the methyl CD1 of Leucine 10

```
#in the search box
L 10 CD1
#output
Atom Searched: LEU 10 CD1 
 Matches found: 
  CD2 LEU 10 2.52
  CD1 LEU 42 3.94
  CG1 VAL 57 4.93
  CG2 VAL 57 4.73
```

Additionally, an output file (data table) is generated for those who wish to manually look through the matches instead of using the scripts search function. 
