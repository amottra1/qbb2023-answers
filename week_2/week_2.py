#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

#Exercise 1: Coverage simulator

def simulate_coverage(coverage, genome_length, read_length, fig_name):
	coverage_array=np.zeros(genome_length)

	num_reads=int(coverage * genome_length / read_length)

	low=0
	high=genome_length-read_length

	start_positions=np.random.randint(low=low, high=high+1, size=num_reads)

	for start in start_positions:
		coverage_array[start: start+read_length]+=1

	#set bins
	x=np.arange(0, max(coverage_array)+1)

	#gives number nonzero coverage
	sim_0cov= genome_length - np.count_nonzero(coverage_array)
	sim_0cov_pct= 100* sim_0cov/genome_length

	print(f'In the simulation, there are {sim_0cov} bases with 0 coverage')
	print(f'This is {sim_0cov_pct}% of the genome')

	# Get poisson distribution
	y_poisson=stats.poisson.pmf(x, mu=coverage) * genome_length
	#print(y_poisson)

	#Get normal distribution
	y_normal= stats.norm.pdf(x, loc=coverage, scale=np.sqrt(coverage)) * genome_length
	#print(y_normal)

	fig, ax = plt.subplots()
	ax.hist(coverage_array, bins=x, align="left", label="Simulation")
	ax.plot(x, y_poisson, label="Poisson")
	ax.plot(x, y_normal, label= "Normal")
	ax.set_xlabel("Coverage")
	ax.set_ylabel("Frequency (bp)")
	ax.set_title("Coverage Simulator")
	ax.legend()
	fig.tight_layout()
	fig.savefig(fig_name)

#Step 1.2

simulate_coverage(3, 1000000, 100, "ex1_3x_cov.png")

#Step 1.4

simulate_coverage(10, 1000000, 100, "ex1_10x_cov.png")

#Step 1.5

simulate_coverage(30, 1000000, 100, "ex1_30x_cov.png")

#Exercise 2: De Bruijn graph construction

#Step 2.1

"""Write code to find all of the edges in the de Bruijn graph corresponding to the 
provided reads using k = 3 (assume all reads are from the forward strand, 
no sequencing errors, complete coverage of the genome). Each edge should be of the format 
ATT -> TTC. Write all edges to a file, with each edge as its own line in the file."""

reads = ['ATTCA', 'ATTGA', 'CATTG', 'CTTAT', 'GATTG', 'TATTT', 'TCATT', 'TCTTA', 'TGATT', 'TTATT', 'TTCAT', 'TTCTT', 'TTGAT']

my_list=[]

k=3

for i in reads:
	for a in range(len(i)-k-1):
		kmer1=i[a:a+k]
		kmer2=i[a+1:a+1+k]
		my_list.append(f'{kmer1} -> {kmer2}')

graph=set(my_list)

f=open("edges.txt", "w")

for line in graph:
	#print(line)
	f.write(line+"\n")












