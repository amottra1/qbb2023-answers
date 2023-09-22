#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

#Step 2.3

reads = ['ATTCA', 'ATTGA', 'CATTG', 'CTTAT', 'GATTG', 'TATTT', 'TCATT', 'TCTTA', 'TGATT', 'TTATT', 'TTCAT', 'TTCTT', 'TTGAT']

my_list=[]

k=3

for i in reads:
	for a in range(len(i)-k):
		kmer1=i[a:a+k]
		kmer2=i[a+1:a+1+k]
		my_list.append(f'{kmer1} -> {kmer2}')

graph=set(my_list)

f=open("edges.dot", "w")
f.write("digraph{")

for line in graph:
	#print(line)
	f.write(line+"\n")

f.write("}")