import re

def checker(pdb_file,pdb_directory,pdb_start,pdb_end,chain,distance_between_atoms,search_parameters,desired_molecules):
    errors=[]
    if pdb_file == ():
        errors.append('No PDB  File Uploaded. Please Upload PDB File and try again. Make sure to use the browse option')
    if pdb_start == ():
        errors.append('Start of sequence has not been defined. Make sure to click ENTER when adding value')
    if pdb_end == ():
        errors.append('End of sequence has not been defined. Make sure to click ENTER when adding value')
    if chain == ():
        errors.append('Chain has not been defined. Make sure to click ENTER when adding value')
    if desired_molecules == []:
        errors.append('No atoms and amino acids picked. Please check which atoms from which amino acids you wish to match to')
    if distance_between_atoms == ():
        errors.append('No Distance defined. Make sure to click ENTER when adding value')
    if search_parameters == ():
        errors.append('No search has been defined. Make sure to click ENTER when adding value')
    else:
        if re.search('\s*([A-Z])\s*(\d+)\s*([A-Z]+\d*)\s*',search_parameters) is None:
            errors.append('Search is in the improper format. Make sure search is in correct format (amino acid type, residue number, atom)')
    return errors
