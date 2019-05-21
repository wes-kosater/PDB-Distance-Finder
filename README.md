# PDB-Distance-Finder

This is a script that I am using as a small component in my wider master's thesis research.

This script will take a PDB file as input, extract all of the alpha carbon positions, read the atomic coordinates, apply an all vs. all Euclidean distance calculation, and output a matrix in the form of a heatmap. 

Note: The script in its current version cannot handle PDB files with AltLocs. I'm looking into ways to fix this. 

### Dependencies
This script uses Biopython 1.73, Pandas, NumPy, SciPy, and Matplotlib.

### How to use
Once you have downloaded the files to your computer, add the PDB files of interest to the directory and run the script with
```
python PDB-Distance-Finder.py
```
### References
Cock PA, Antao T, Chang JT, Chapman BA, Cox CJ, Dalke A, Friedberg I, Hamelryck T, Kauff F, Wilczynski B and de Hoon MJL (2009) Biopython: freely available Python tools for computational molecular biology and bioinformatics. Bioinformatics, 25, 1422-1423

Stéfan van der Walt, S. Chris Colbert and Gaël Varoquaux. The NumPy Array: A Structure for Efficient Numerical Computation, Computing in Science & Engineering, 13, 22-30 (2011), DOI:10.1109/MCSE.2011.37 

John D. Hunter. Matplotlib: A 2D Graphics Environment, Computing in Science & Engineering, 9, 90-95 (2007), DOI:10.1109/MCSE.2007.55

Hamelryck, T., Manderick, B. (2003) PDB parser and structure class implemented in Python. Bioinformatics 19: 2308–2310

Wes McKinney. Data Structures for Statistical Computing in Python, Proceedings of the 9th Python in Science Conference, 51-56 (2010) 
