#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 18:54:44 2019
"""

from Bio.PDB import *
import pandas as pd
from scipy.spatial.distance import squareform, pdist
import re
import matplotlib.pyplot as plt
import numpy as np
import datetime
import sys

#This uses regular expressions to extract each CA from the chain file and write it to CA.txt
def CA(chain):
    e = open('CA-' + chain + '.txt', 'w')
    f = open(chain, 'r')

    for record in f:
        if(re.search(r'^ATOM\s+\d+\s+CA\s+[ADTSEPGCVMILYFHKRWQN]', record)): 
            e.write(record)

    e.close()
    f.close()      

#This function generates the heatmap. Credit to Huang Yuheng, StackOverflow
def heatmap(arr: np.ndarray):           
    currentDT = datetime.datetime.now()
    plt.imshow(arr, cmap='viridis')
    plt.colorbar()
    plt.savefig(currentDT.strftime("%H:%M:%S"))

pdbID = input('Enter PDB ID (ex. 1fkq) ')

parser=PDBParser()
io=PDBIO()
structure=parser.get_structure('X', pdbID+'.pdb')
try:
    for chain in structure.get_chains():
        io.set_structure(chain)
        io.save(chain.get_id() + ".pdb")
        print(chain.get_id())
except:
    sys.exit('This PDB file containns AltLocs. These are not currently supported.')

print('PDB files generated')
chain = input('Select chain to use: ')
CA(chain + '.pdb')


arr_coord = []

for chains in structure:
    for chain in chains:
        for residue in chain:                             
            for atom in residue:
                x = atom.get_coord()
                arr_coord.append({'X': x[0],'Y':x[1],'Z':x[2]}) 

coord_table = pd.DataFrame(arr_coord)

print('Generating distance matrix. Please wait...')

#Distance matrix generation
dist = pdist(coord_table, metric = 'euclidean')
distance_matrix = squareform(dist)
print('Distances Calculated')

heatmap(distance_matrix)