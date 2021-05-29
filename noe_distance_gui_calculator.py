import re
import math
import os


####SCRIPT START###

conversion={'A':'ALA','R':'ARG','N':'ASN','D':'ASP','C':'CYS','G':'GLY','V':'VAL','Y':'TYR','W':'TRP','T':'THR','S':'SER','P':'PRO','F':'PHE','M':'MET','K':'LYS','L':'LEU','I':'ILE','H':'HIS','Q':'GLN','E':'GLU'}

def create_data(pdb_file,pdb_directory,pdb_start,pdb_end,chain,distance_between_atoms,search_parameters,desired_molecules):
    aa_name=[]
    aa_position=[]
    os.chdir(pdb_directory)
    word=' '.join(search_parameters.split()[0:2])
    atom=search_parameters.split()[2]
    amino_acid=word.split()
    amino_acid[0]=conversion[amino_acid[0]]
    desired_molecules.append(atom+' '+amino_acid[0])
    with open(pdb_file) as pdb_files:
        for lines in pdb_files:
            chain_search=re.search(f'(\w+\s+(\w+){{3}})\s+{chain}\s+(\d+)\s+((\d+\.\d+\s+){{3}})',lines)
            if chain_search != None:
                if int(chain_search.group(3)) > int(pdb_start) and int(chain_search.group(3)) < int(pdb_end):
                    if (' '.join(chain_search.group(1).split())) in desired_molecules:
                        aa_name.append(' '.join(chain_search.group(1,3)))
                        aa_position.append(chain_search.group(4))


    value_holder=[]
    number_holder=[]
    with open('output.txt','w') as output_file:
        for name,position in zip(aa_name,aa_position):
            for name2,position2 in zip(aa_name,aa_position):
                coordinates_1=position.split()
                coordinates_2=position2.split()
                distance=(((float(coordinates_1[0])-float(coordinates_2[0]))**2)+((float(coordinates_1[1])-float(coordinates_2[1]))**2)+((float(coordinates_1[2])-float(coordinates_2[2]))**2))
                if distance>0:
                    sqrt_distance=math.sqrt(distance)
                    if sqrt_distance<float(distance_between_atoms):
                        value_holder.append(name2)
                        number_holder.append(str(round(sqrt_distance,2)))
            output_file.write(f'{name} {" ".join(value_holder)} {" ".join(number_holder)}\n')
            value_holder.clear()
            number_holder.clear()

list0=[]
list1=[]
list2=[]
list3=[]

def data_table(pdb_file,pdb_directory,pdb_start,pdb_end,chain,distance_between_atoms,search_parameters,desired_molecules):
    global list0
    global list1
    global list2
    global list3
    with open('output.txt') as file:
        for lines in file:
            a=lines.split()
            temp_list=[]
            counter=0
            for values in a:
                float_checker=re.search('\d+\.\d+',values)
                if float_checker != None:
                    list3.append(float_checker.group(0))
                    continue
                counter+=1
                if counter == 1:
                    list1.append(values)
                if counter < 3 and counter > 1:
                    temp_list.append(values)
                if counter == 3:
                    temp_list.append(values)
                    list0.append((' '.join(temp_list)))
                    temp_list.clear()
                if counter > 3:
                    temp_list.append(values)
                if counter == 6:
                    list0.append('')
                    list1.append('')
                    list2.append((' '.join(temp_list)))
                    temp_list.clear()
                    counter=3
            list0.pop(-1)
            list1.pop(-1)

def search_table(pdb_file,pdb_directory,pdb_start,pdb_end,chain,distance_between_atoms,search_parameters,desired_molecules):
    global list0
    global list1
    global list2
    global list3
    create_data(pdb_file,pdb_directory,pdb_start,pdb_end,chain,distance_between_atoms,search_parameters,desired_molecules)
    data_table(pdb_file,pdb_directory,pdb_start,pdb_end,chain,distance_between_atoms,search_parameters,desired_molecules)
    word=' '.join(search_parameters.split()[0:2])
    atom=search_parameters.split()[2]
    matches_list=[]
    amino_acid=word.split()
    amino_acid[0]=conversion[amino_acid[0]]
    word=' '.join(amino_acid)
    counter=0
    for residue,atom_type,correlation,distance in zip(list0,list1,list2,list3):
        word_search=re.search(word,residue)
        atom_search=re.search(atom,atom_type)
        if counter == 1:
            if residue != '':
                break
            else:
                matches_list.append(f'{residue} {atom_type} {correlation} {distance}')
        if word_search != None and atom_search != None:
            counter+=1
            matches_list.append(f'Atom Searched: {residue} {atom_type} \n  Matches found: \n  {correlation} {distance}')
    list0.clear()
    list1.clear()
    list2.clear()
    list3.clear()
    return matches_list
