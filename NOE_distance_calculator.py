import re
import math
import os

"""
Paramaters

start and end are the bounadaries of regions you want to search in your pdb file  (e.g. if you only want a singular domain 144-340)
pdb file is self explanatory
distance between atoms is the distance (in angstroms) that it will search and display
The desired atoms is a table of selected atoms to display, if you want to display every atom within your distance, leave it empty. To add entries, add them in this format 'atom 3-letter abr amino acid' I.E. 'CD1 LEU'
So your desired_atoms would look like ['CD1 LEU','CD2 LEU','N LEU']
"""
start=1
end=243
pdb_file='1mmi.pdb'
distance_between_atoms=5
desired_atoms=['CD1 LEU','CD2 LEU','CG1 VAL','CG2 VAL','N LEU','N VAL','N ILE','CD1 ILE']




####SCRIPT START###

conversion={'A':'ALA','R':'ARG','N':'ASN','D':'ASP','C':'CYS','G':'GLY','V':'VAL','Y':'TYR','W':'TRP','T':'THR','S':'SER','P':'PRO','F':'PHE','M':'MET','K':'LYS','L':'LEU','I':'ILE','H':'HIS','Q':'GLN','E':'GLU'}

def create_data():
    aa_name=[]
    aa_position=[]
    with open(pdb_file) as pdb_file:
        for lines in pdb_file:
            chain_search=re.search('(\w+\s+(\w+){3})\s+A\s+(\d+)\s+((\d+\.\d+\s+){3})',lines)
            if chain_search != None:
                if int(chain_search.group(3)) > start and int(chain_search.group(3)) < end:
                    if (' '.join(chain_search.group(1).split())) in desired_atoms:
                        aa_name.append(' '.join(chain_search.group(1,3)))
                        aa_position.append(chain_search.group(4))
                        continue
                    if desired_atoms == []:
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
                    if sqrt_distance<distance_between_atoms:
                        value_holder.append(name2)
                        number_holder.append(str(round(sqrt_distance,2)))
            output_file.write(f'{name} {" ".join(value_holder)} {" ".join(number_holder)}\n')
            value_holder.clear()
            number_holder.clear()

list0=[]
list1=[]
list2=[]
list3=[]

def data_table():
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

def search_table(word,atom):
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
                print(residue,atom_type,correlation,distance)
        if word_search != None and atom_search != None:
            counter+=1
            print(residue,atom_type,correlation,distance)


def make_table():
    import pandas as pd

    d={'Residue':[],'Atom Type':[],'Correlation':[],'Distance(A)':[]}

    d['Residue']=list0
    d['Atom Type']=list1
    d['Correlation']=list2
    d['Distance(A)']=list3

    df=pd.DataFrame.from_dict(d)
    view=df.replace('', method='ffill').query('Residue == "LEU 241"')
    view.loc[ view.duplicated('Residue'), 'Residue' ] = ''
    #pd.set_option('display.max_rows', None)
    df.to_csv(r'data_table.txt',sep='\t')

def main_loop():
    create_data()
    data_table()
    make_table()
    while True:
        question=(input('amino number atom (i.e. I 166 CD1). When finished, type quit to exit: ').split())
        try:
            if question[0] == 'quit':
                os.remove('output.txt')
                break
            search_table((' '.join(question[0:2])),question[2])
        except:
            print('Invalid entry\nTry Again')

main_loop()
