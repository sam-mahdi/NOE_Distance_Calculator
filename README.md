# NOE_Distance_Calculator
Uses a PDB file to calculate NOE distances within a desired distance for desired atoms

The parameters to modify in the script:

start and end are the bounadaries of regions you want to search in your pdb file  (e.g. if you only want a singular domain 144-340)
pdb file is self explanatory
distance between atoms is the distance (in angstroms) that it will search and display
The desired atoms is a table of selected atoms to display, if you want to display every atom within your distance, leave it empty. To add entries, add them in this format 'atom 3-letter abr amino acid' I.E. 'CD1 LEU'
So your desired_atoms would look like ['CD1 LEU','CD2 LEU','N LEU']

Additionally, an output file (data table) is generated for those who wish to manually look through the matches instead of using the scripts search function. 
