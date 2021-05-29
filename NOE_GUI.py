from tkinter import *
import tkinter.scrolledtext as st
from tkinter import ttk
import functools

root = Tk()

class ReadOnlyText(st.ScrolledText):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(state=DISABLED)

        self.insert = self._unlock(super().insert)
        self.delete = self._unlock(super().delete)

    def _unlock(self, f):
        @functools.wraps(f)
        def wrap(*args, **kwargs):
            self.config(state=NORMAL)
            r = f(*args, **kwargs)
            self.config(state=DISABLED)
            return r
        return wrap


ttk.Label(root,text = "Program Output",font = ("Times New Roman", 15),background = 'green',foreground = "white").grid(column = 0, row = 15)

text_area = ReadOnlyText(root,width = 60,height = 15,font = ("Times New Roman",12))

text_area.grid(column = 0,columnspan=3,sticky=W+E,pady = 10, padx = 10)

def desired_amino_acids():
    amino_acid_list=[]
    if ALA.get()!=0:
        amino_acid_list.append('ALA')
    if ARG.get()!=0:
        amino_acid_list.append('ARG')
    if ASN.get()!=0:
        amino_acid_list.append('ASN')
    if ASP.get()!=0:
        amino_acid_list.append('ASP')
    if CYS.get()!=0:
        amino_acid_list.append('CYS')
    if GLN.get()!=0:
        amino_acid_list.append('GLN')
    if GLU.get()!=0:
        amino_acid_list.append('GLU')
    if GLY.get()!=0:
        amino_acid_list.append('GLY')
    if HIS.get()!=0:
        amino_acid_list.append('HIS')
    if ILE.get()!=0:
        amino_acid_list.append('ILE')
    if LEU.get()!=0:
        amino_acid_list.append('LEU')
    if LYS.get()!=0:
        amino_acid_list.append('LYS')
    if MET.get()!=0:
        amino_acid_list.append('MET')
    if PHE.get()!=0:
        amino_acid_list.append('PHE')
    if PRO.get()!=0:
        amino_acid_list.append('PRO')
    if SER.get()!=0:
        amino_acid_list.append('SER')
    if THR.get()!=0:
        amino_acid_list.append('THR')
    if TRP.get()!=0:
        amino_acid_list.append('TRP')
    if TYR.get()!=0:
        amino_acid_list.append('TYR')
    if VAL.get()!=0:
        amino_acid_list.append('VAL')
    return amino_acid_list

def desired_atoms():
    atom_list=[]
    if nitrogen.get()!=0:
        atom_list.append('N')
    if alpha_carbon.get()!=0:
        atom_list.append('CA')
    if beta_carbon.get()!=0:
        atom_list.append('CB')
    if gamma_carbon.get()!=0:
        atom_list.append('CG')
    if gamma_carbon1.get()!=0:
        atom_list.append('CG1')
    if gamma_carbon2.get()!=0:
        atom_list.append('CG2')
    if delta_carbon.get()!=0:
        atom_list.append('CD')
    if delta_carbon1.get()!=0:
        atom_list.append('CD1')
    if delta_carbon2.get()!=0:
        atom_list.append('CD2')
    if epsilon_carbon.get()!=0:
        atom_list.append('CE')
    if epsilon_carbon1.get()!=0:
        atom_list.append('CE1')
    if epsilon_carbon2.get()!=0:
        atom_list.append('CE2')
    if gln_nitrogen.get()!=0:
        atom_list.append('NE2')
    if asn_nitrogen.get()!=0:
        atom_list.append('ND2')
    return atom_list

pdb_file=()
pdb_directory=()
pdb_start=()
pdb_end=()
chain=()
distance_between_atoms=()
search_parameters=()

def distance_constraint():
    global distance_between_atoms
    distance_between_atoms=distance_value.get()

def search():
    global search_parameters
    search_parameters=query.get()

def clear():
    text_area.delete(1.0,END)
    
conversion={'A':'ALA','R':'ARG','N':'ASN','D':'ASP','C':'CYS','G':'GLY','V':'VAL','Y':'TYR','W':'TRP','T':'THR','S':'SER','P':'PRO','F':'PHE','M':'MET','K':'LYS','L':'LEU','I':'ILE','H':'HIS','Q':'GLN','E':'GLU'}
    

def main():
    from pdb_upload_window import variables
    global pdb_file
    global pdb_directory
    global pdb_start
    global pdb_end
    global chain
    pdb_file,pdb_directory,pdb_start,pdb_end,chain=variables()
    atoms=desired_atoms()
    amino_acids=desired_amino_acids()
    desired_molecules=[]
    for atom in atoms:
        for amino_acid in amino_acids:
            desired_molecules.append(atom+' '+amino_acid)   
    from check_files import checker
    error_list=checker(pdb_file,pdb_directory,pdb_start,pdb_end,chain,distance_between_atoms,search_parameters,desired_molecules)
    if error_list != []:
        for errors in error_list:
            text_area.insert(INSERT, errors+'\n')
        text_area.insert(INSERT, 'Please correct above errors and rerun\n')
    else:
        remove_flag=False
        word=' '.join(search_parameters.split()[0:2])
        atom=search_parameters.split()[2]
        amino_acid=word.split()
        amino_acid[0]=conversion[amino_acid[0]]
        if (atom+' '+amino_acid[0]) not in desired_molecules:
            remove_flag=True
        from noe_distance_gui_calculator import search_table
        matches_list=search_table(pdb_file,pdb_directory,pdb_start,pdb_end,chain,distance_between_atoms,search_parameters,desired_molecules)
        if len(matches_list) == 0:
            text_area.insert(INSERT, 'No matches found\n')
        for matches in matches_list:
            if remove_flag is True:
                if ' '.join(matches.split()[0:2]) == (atom+' '+amino_acid[0]):
                    continue
            text_area.insert(INSERT, matches+'\n')


def pdb_window():
    from pdb_upload_window import newTopLevel
    new_top = newTopLevel(root)
    newWindow = new_top.newWindow

ALA= IntVar()
ARG= IntVar()
ASN= IntVar()
ASP= IntVar()
CYS= IntVar()
GLN= IntVar()
GLU= IntVar()
GLY= IntVar()
HIS= IntVar()
ILE= IntVar()
LEU= IntVar()
LYS= IntVar()
MET= IntVar()
PHE= IntVar()
PRO= IntVar()
SER= IntVar()
THR= IntVar()
TRP= IntVar()
TYR= IntVar()
VAL= IntVar()
nitrogen= IntVar()
alpha_carbon= IntVar()
beta_carbon= IntVar()
gamma_carbon= IntVar()
gamma_carbon1= IntVar()
gamma_carbon2= IntVar()
delta_carbon= IntVar()
delta_carbon1= IntVar()
delta_carbon2= IntVar()
epsilon_carbon= IntVar()
epsilon_carbon1= IntVar()
epsilon_carbon2= IntVar()
gln_nitrogen= IntVar()
asn_nitrogen= IntVar()
Label(root, text='Atoms').grid(row=0, sticky=W)
Label(root, text='Amino acids').grid(row=0,column=1, sticky=W)
Label(root, text='Distance').grid(row=11,column=1, sticky=W)
distance_value=Entry(root)
distance_value.grid(row=11,column=2,sticky=W)
Label(root, text='Search (e.g. I 166 CD1)').grid(row=12,column=1, sticky=W)
query=Entry(root)
query.grid(row=12,column=2,sticky=W)
Checkbutton(root, text="ALA", variable=ALA).grid(row=1,column=1, sticky=W)
Checkbutton(root, text="ARG", variable=ARG).grid(row=2,column=1, sticky=W)
Checkbutton(root, text="ASN", variable=ASN).grid(row=3,column=1, sticky=W)
Checkbutton(root, text="CYS", variable=CYS).grid(row=4,column=1, sticky=W)
Checkbutton(root, text="GLN", variable=GLN).grid(row=5,column=1, sticky=W)
Checkbutton(root, text="GLU", variable=GLU).grid(row=6,column=1, sticky=W)
Checkbutton(root, text="GLY", variable=GLY).grid(row=7,column=1, sticky=W)
Checkbutton(root, text="HIS", variable=HIS).grid(row=8,column=1, sticky=W)
Checkbutton(root, text="ILE", variable=ILE).grid(row=9,column=1, sticky=W)
Checkbutton(root, text="LEU", variable=LEU).grid(row=10,column=1, sticky=W)
Checkbutton(root, text="LYS", variable=LYS).grid(row=1,column=2, sticky=W)
Checkbutton(root, text="MET", variable=MET).grid(row=2,column=2, sticky=W)
Checkbutton(root, text="PHE", variable=PHE).grid(row=3,column=2, sticky=W)
Checkbutton(root, text="PRO", variable=PRO).grid(row=4,column=2, sticky=W)
Checkbutton(root, text="SER", variable=SER).grid(row=5,column=2, sticky=W)
Checkbutton(root, text="THR", variable=THR).grid(row=6,column=2, sticky=W)
Checkbutton(root, text="TRP", variable=TRP).grid(row=7,column=2, sticky=W)
Checkbutton(root, text="TYR", variable=TYR).grid(row=8,column=2, sticky=W)
Checkbutton(root, text="VAL", variable=VAL).grid(row=9,column=2, sticky=W)
Checkbutton(root, text="N", variable=nitrogen).grid(row=1,column=0, sticky=W)
Checkbutton(root, text="CA", variable=alpha_carbon).grid(row=2,column=0, sticky=W)
Checkbutton(root, text="CB", variable=beta_carbon).grid(row=3,column=0, sticky=W)
Checkbutton(root, text="CG", variable=gamma_carbon).grid(row=4,column=0, sticky=W)
Checkbutton(root, text="CG1", variable=gamma_carbon1).grid(row=5,column=0, sticky=W)
Checkbutton(root, text="CG2", variable=gamma_carbon2).grid(row=6,column=0, sticky=W)
Checkbutton(root, text="CD", variable=delta_carbon).grid(row=7,column=0, sticky=W)
Checkbutton(root, text="CD1", variable=delta_carbon1).grid(row=8,column=0, sticky=W)
Checkbutton(root, text="CD2", variable=delta_carbon2).grid(row=9,column=0, sticky=W)
Checkbutton(root, text="CE", variable=epsilon_carbon).grid(row=10,column=0, sticky=W)
Checkbutton(root, text="CE1", variable=epsilon_carbon1).grid(row=11,column=0, sticky=W)
Checkbutton(root, text="CE2", variable=epsilon_carbon2).grid(row=12,column=0, sticky=W)
Checkbutton(root, text="GLN NH2", variable=gln_nitrogen).grid(row=13,column=0, sticky=W)
Checkbutton(root, text="ASN NH2", variable=asn_nitrogen).grid(row=14,column=0, sticky=W)

Button(root, text='Quit', command=root.quit).grid(row=13,column=3, sticky=W)
Button(root, text='Run', command=main).grid(row=13,column=2, sticky=W)
Button(root, text='Enter', command=distance_constraint).grid(row=11,column=3, sticky=W)
Button(root, text='Enter', command=search).grid(row=12,column=3, sticky=W)
Button(root, text='Clear', command=clear).grid(row=13,column=1, sticky=W)
Button(root, text='Upload PDB File', command=pdb_window).grid(row=1,column=3)
mainloop()
