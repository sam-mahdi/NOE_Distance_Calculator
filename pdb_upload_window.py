from tkinter import *
from tkinter import filedialog
import os

pdb_file=()
pdb_directory=()
pdb_start=()
pdb_end=()
chain=()

class newTopLevel(object):
    def __init__(self, root):
        self.newWindow = Toplevel(root)
        self.newWindow.title("PDB File Upload")
        self.newWindow.geometry("600x600")
        Label(self.newWindow, text="PDB File\n Use Browse Button").grid(row=0)
        self.pdb_line = Entry(self.newWindow)
        self.pdb_line.grid(row=0, column=1)
        self.newWindow.btn = Button(self.newWindow,text='browse',command=self.input_pdb)
        self.newWindow.btn.grid(row=0,column=2)
        Label(self.newWindow, text="Start of desired sequence\n Make sure to click enter").grid(row=1)
        self.pdb_start_line = Entry(self.newWindow)
        self.pdb_start_line.grid(row=1, column=1)
        self.newWindow.btn = Button(self.newWindow,text='enter',command=self.pdb_start_input)
        self.newWindow.btn.grid(row=1,column=2)
        Label(self.newWindow, text="End of desired sequence\n Make sure to click enter").grid(row=2)
        self.pdb_end_line = Entry(self.newWindow)
        self.pdb_end_line.grid(row=2, column=1)
        self.newWindow.btn = Button(self.newWindow,text='enter',command=self.pdb_end_input)
        self.newWindow.btn.grid(row=2,column=2)
        Label(self.newWindow, text="Protein Chain\n Make sure to click enter").grid(row=3)
        self.pdb_chain_line = Entry(self.newWindow)
        self.pdb_chain_line.grid(row=3, column=1)
        self.newWindow.btn = Button(self.newWindow,text='enter',command=self.pdb_chain_input)
        self.newWindow.btn.grid(row=3,column=2)



    def input_pdb(self):
        fullpath = filedialog.askopenfilename(parent=self.newWindow, title='Choose a file')
        global pdb_file
        global pdb_directory
        pdb_directory=os.path.dirname(fullpath)
        pdb_file= os.path.basename(fullpath)
        label3=Label(self.newWindow,text=fullpath).grid(row=0,column=1)

    def pdb_start_input(self):
        pdb_start_inputs=self.pdb_start_line.get()
        global pdb_start
        pdb_start=float(pdb_start_inputs)

    def pdb_end_input(self):
        pdb_end_inputs=self.pdb_end_line.get()
        global pdb_end
        pdb_end=float(pdb_end_inputs)

    def pdb_chain_input(self):
        pdb_chain_inputs=self.pdb_chain_line.get()
        global chain
        chain=pdb_chain_inputs

def variables():
    return pdb_file,pdb_directory,pdb_start,pdb_end,chain
