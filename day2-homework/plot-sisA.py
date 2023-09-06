#!/usr/bin/env python

import numpy as np 

import matplotlib.pyplot as plt

#Excercise 1
"""Starting with plot-sxl.py, create plot-sisA.py to visualize sisA (FBtr0073461) 
in a fashion similar to Lott et al 2011 PLoS Biology Fig 3A 
by adding elements in the following order. 
After each step, push your code and plot to your git repository and check your repository 
using the https://github.com web interface (i.e. results in four separate commits)."""

"""Plot female data
Add male data
Add 2*male data (HINT: 2 * np.array( y ))
Annotate plot (generalize x-axis to 10 not female_10, add title, add x- and y-axis labels)"""

#For Commit 1: Plot female data
#For Commit 2: Add male data

transcripts = np.loadtxt( "all_annotated.csv", delimiter=",", usecols=0, dtype="<U30", skiprows=1 )
print( "transcripts: ", transcripts[0:5] )

samples = np.loadtxt( "all_annotated.csv", delimiter=",", max_rows=1, dtype="<U30" )[2:]
print( "samples: ", samples[0:5] )

data = np.loadtxt( "all_annotated.csv", delimiter=",", dtype=np.float32, skiprows=1, usecols=range(2, len(samples) + 2) )
print( "data: ", data[0:5, 0:5] )

# Find row with transcript of interest
for i in range(len(transcripts)):
    if transcripts[i] == 'FBtr0073461':
        row = i

# Find columns with samples of interest
cols = []
for i in range(len(samples)):
    if "female" in samples[i]:
        cols.append(i)

#add males as new set of data
colsm = []
for im in range(len(samples)):
    if "female" not in samples[im]:
        colsm.append(im)

# Subset data of interest
expression = data[row, cols]
expressionm = data[row, colsm]

# Prepare data
x = samples[cols]
y = expression
ym =expressionm

#Plot data
fig, ax = plt.subplots()
ax.set_title( "FBtr0073461" )
ax.plot( x, y )
ax.plot(x, ym) #add male data

plt.xticks(rotation=90) #rotate x-axis labels
ax.set_title( "Sxl (FBtr0073461)" ) #rename title
ax.set_xlabel( "Developmental Stage") #set x-axis label
ax.set_ylabel("mRNA Abundance (RPKM)") #set y-axis label



plt.tight_layout()
fig.savefig( "FBtr0073461.png" )
plt.show()
plt.close( fig )










