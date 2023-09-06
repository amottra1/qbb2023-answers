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
#For Commit 3: Add 2*male data (HINT: 2 * np.array( y ))
#For Commit 4: Annotate plot (generalize x-axis to 10 not female_10, add title, add x- and y-axis labels)

#Exercise 2
"""Modify plot-sisA.py (do not create a new file) to load the transcripts information 
using open() and a for loop rather than np.loadtxt(). Remember that the first line is a header 
and should not be stored in the transcripts list. Push just your code to your git repository 
and confirm at https://github.com that your code no longer uses np.loadtxt()."""

f= open("all_annotated.csv", "r")

lines=f.readlines()

datalist=[]

for line in lines:
	line=line.rstrip()
	line_list=line.split(',')
	datalist.append((line_list))

#print(datalist)

transcripts=[]
for value in datalist:
	transcripts.append(value[0])

#print(transcripts)


#mute old way for transcripts
"""transcripts = np.loadtxt( "all_annotated.csv", delimiter=",", usecols=0, dtype="<U30", skiprows=1 )
print( "transcripts: ", transcripts[0:5] )"""

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

expressionm2 = 2 * np.array(expressionm)

# Prepare data
x = samples[cols]
y = expression
ym =expressionm
ym2 =expressionm2

#Generalize x-axis labels

xc = ["10", "11", "12", "13", "14A", "14B", "14C", "14D"]

#Plot data
fig, ax = plt.subplots()
ax.set_title( "FBtr0073461" )
ax.plot( xc, y , label="female")
ax.plot(xc, ym, label="male") #add male data
ax.plot(xc, ym2, label="male*2") #add 2*male data

plt.xticks(rotation=90) #rotate x-axis labels
ax.set_title( "Sxl (FBtr0073461)" ) #rename title
ax.set_xlabel( "Developmental Stage") #set x-axis label
ax.set_ylabel("mRNA Abundance (RPKM)") #set y-axis label

ax.legend()

plt.tight_layout()
fig.savefig( "FBtr0073461.png" )
plt.show()
plt.close( fig )










