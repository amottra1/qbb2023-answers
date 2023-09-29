#!usr/bin/env python

import numpy as np
import sys

import pandas as pd

from fasta import readFASTA

#Exercise 1: Needleman-Wunsch Algorithm

"""Write a script to perform global alignment between two sequences 
using a given scoring matrix and gap penalty. Your script will take 
four inputs:

A FASTA-style file containing two sequences to align
A text file containing the scoring matrix you’d like to use for this 
alignment
The penalty for gaps in your alignment (so if users wanted to penalize 
gaps by subtracting 10 from the alignment score, they would input -10)
The filepath to write your alignment to
Additionally, your script should print out the number of gaps in the 
first sequence, the number of gaps in the second sequence, and the 
score of the final alignment.

You’ll run your script twice:

Align the CTCF DNA transcript sequences from human and mouse using the 
HOXD70 scoring matrix and a gap penalty of -300.
Align the CTCF amino acid sequences from human and mouse using the 
BLOSUM62 scoring matrix and a gap penalty of -10.
NOTE: The DNA sequences are fairly long, and as such the DNA alignment 
may take a few minutes to run. We recommend testing your code with the
protein alignment first (or even just a couple of small test sequences),
 and then running the DNA alignment when you’re confident it’s working."""

#Step 1.1: Read in your parameters

fasta_file=sys.argv[1]
scoring_file=sys.argv[2]
gap_penalty=float(sys.argv[3])
filepath=sys.argv[4]
name_type=sys.argv[5]

input_sequences = readFASTA(open(fasta_file))

seq1_id, sequence1 = input_sequences[0]
seq2_id, sequence2 = input_sequences[1]

#print(sequence1)
#print(sequence2)

scoring_matrix=pd.read_csv(scoring_file,delimiter=r"\s+")

#print(scoring_matrix)

#Step 1.2: Initializing matrices

"""You’ll need two matrices to carry out the Needleman-Wunsch algorithm: 
an F-matrix that stores the score of each “optimal” sub-alignment 
(this is the one we created in class), as well as a traceback matrix that 
allows you to determine the optimal global alignment (as a path through this 
matrix). Initialize two empty matrices for these purposes.

HINT: With sequence 1 of length m and sequence 2 of length n, both matrices 
should be of size (m+1)×(n+1), to account for potential leading gaps in either 
sequence."""

f_matrix=np.zeros((len(sequence1)+1, len(sequence2)+1))
trace_matrix=np.zeros((len(sequence1)+1, len(sequence2)+1))

#Step 1.3: Populating the matrices

"""Follow the steps of the needleman-wunsch algorithm discussed in 
class to populate the two matrices.

When generating the traceback matrix: if at any point there is a tie between 
aligning, a gap in sequence 1, or a gap in sequence 2, resolve the tie in the 
order (aligning -> gap in sequence 1 -> gap in sequence 2)."""

for i in range(f_matrix.shape[0]):
	f_matrix[i,0]= i * gap_penalty

for j in range(f_matrix.shape[1]):
	f_matrix[0,j]= j * gap_penalty

for i in range(1,f_matrix.shape[0]):
	for j in range(1, f_matrix.shape[1]):
		h= f_matrix[i, j-1] + gap_penalty
		v= f_matrix[i-1,j] + gap_penalty
		#reference by Panda scoring_matrix.loc[index/row,"column name"]
		d=f_matrix[i-1,j-1]+ scoring_matrix.loc[sequence1[i-1],sequence2[j-1]]
		#print(scoring_matrix.loc[sequence1[i-1],sequence2[j-1]])
		max_val=max(d,h,v) #order of list is order of preference for selection if ties
		f_matrix[i,j]=max_val
		if max(h,v,d)==h:
			trace_matrix[i,j]=0
		elif max(h,v,d)==v:
			trace_matrix[i,j]=1
		elif max(h,v,d)==d:
			trace_matrix[i,j]=2

#print(scoring_matrix)
#print(f_matrix)
#print(trace_matrix)

#Step 1.4: Find the optimal alignment

"""Use the traceback matrix to find the optimal alignment between the 
two sequences. Start at the bottom right corner and follow a path backwards 
through the traceback matrix until you reach the top left of the matrix, 
building the alignment as you go. You should end up with two strings of 
the same length, one for each sequence. Gaps in the sequences should be denoted 
with a hyphen (-). For example, if your input sequences were TACGATTA and 
ATTAACTTA your final alignment might look something like:
Sequence 1 alignment: '--TACGA-TTA'
Sequence 2 alignment: 'ATTA--ACTTA

HINT: A while loop will probably be helpful for this part.'"""

#print out the number of gaps in the first sequence, 
#the number of gaps in the second sequence, 
#and the score of the final alignment

sequence1_align=[]
sequence2_align=[]

i=f_matrix.shape[0]-1
j=f_matrix.shape[1]-1
k=len(sequence1)-1
m=len(sequence2)-1
x=0 #gaps in seq 1
y=0 #gaps in seq 2

#remember h=0(to left), v=1(up 1) and d=2(up1 and to left)

while i>0 or j>0:
	if trace_matrix[i,j]==2: #d
		sequence1_align.append(sequence1[k])
		sequence2_align.append(sequence2[m])
		k-=1
		m-=1
		i-=1
		j-=1
	elif trace_matrix[i,j]==1: #v
		sequence1_align.append(sequence1[k])
		k-=1
		i-=1
		sequence2_align.append("_")
		y+=1
	elif trace_matrix[i,j]==0: #h
		sequence1_align.append("_")
		x+=1
		sequence2_align.append(sequence2[m])
		m-=1
		j-=1


sequence1_align.reverse()
sequence2_align.reverse()

#print("Sequence 1 is:", "".join(sequence1_align))
#print("Sequence 2 is:", "".join(sequence2_align))
#print("Gaps in Sequence 1 is:", x)
#print("Gaps in Sequence 2 is:", y)
#print("Final alignment score is:", f_matrix[f_matrix.shape[0]-1,f_matrix.shape[1]-1])

#Step 1.5: Write the alignment to the output
"""Write the alignment to the output file specified in the command line.

ALSO, make sure your script prints out the additional requested information:

the number of gaps in each sequence and
the score of the alignment
For both alignments (DNA and AA), record these values in your README.md."""

#sys.argv[5] name type
#sys.argv[4] file to write to

x_string=str(x)
y_string=str(y)
align_string=str(f_matrix[f_matrix.shape[0]-1,f_matrix.shape[1]-1])

f=open(sys.argv[4], "a")
f.write("\n"+sys.argv[5]+"\n")
f.write("Sequence 1 is:\n")
f.write("".join(sequence1_align))
f.write("\nSequence 2 is:\n")
f.write("".join(sequence2_align))
f.write("\nGaps in Sequence 1 is: ")
f.write(x_string)
f.write("\nGaps in Sequence 2 is: ")
f.write(y_string)
f.write("\nFinal alignment score is: ")
f.write(align_string+"\n")










