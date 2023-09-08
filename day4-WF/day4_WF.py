#Exercise 1:

#pick starting frequency for allele and pop size - input parameters of fxn

#make list to store allele freq

#While our allele freq is between 0 and 1:
	#get new allele freq for next gen
	#draw from numpy.random.binomial(n,p)
	#we get # of successes out of random binomial
	#need to convert # successes to a allele freq

	#want to store allele freq in allele freq list

#return a list of allele freq at each time point (aka each gen)
#add to plot where x axis is gen and y axis is freq at that gen
#num of gens to fixation will be length of list

import numpy as np

import matplotlib.pyplot as plt


def pop_dyn(start_freq, pop_size):
	allele_freq=[start_freq]
	while 0<allele_freq[-1]<1:
		new_succ=np.random.binomial(2*pop_size,allele_freq[-1])
		new_freq=new_succ/(2*pop_size)
		allele_freq.append(new_freq)
	return (allele_freq)

result=pop_dyn(0.5,100)
gens=len(result)
print(gens)

fig, ((ax1,ax2, ax6),(ax3,ax4, ax5)) = plt.subplots(2,3)
#use ax6 as empty plot to make plots easier to view

x_values=range(len(result))

y_values=[]
for i in range(len(result)):
	y_values.append(result[i])

ax1.plot(x_values, y_values)
ax1.set_title( "Allele Frequency over time" )
ax1.set_xlabel( "Generation") 
ax1.set_ylabel("Allele Frequency") 


#Exercise 2

"""Because sampling from the binomial distribution is random, 
the behavior of this model changes every time that we run it. 
(To view this, run  np.random.binomial(n, p) a few times on your own 
and see how the numbers vary). Run your model repeatedly 
(at least 30 iterations) and visualize all your allele frequency trajectories
 together on one plot. Remember that you can lines to a matplotlib figure 
 using a for loop.

Run your model at least 1000 times and create a histogram of the times 
to fixation. If you want to see the distribution of times to fixation, 
this is an effective way of doing so."""

many_runs=[]

for i in range(30):
	result_2=pop_dyn(0.5,100)

	ax2.plot(range(len(result_2)),result_2)

ax2.set_title( "Allele Frequency over time- several tries" )
ax2.set_xlabel( "Generation") 
ax2.set_ylabel("Allele Frequency") 

#for histogram
num_gens=[]

for c in range(1000):
	result_3=pop_dyn(0.5,100)
	gens=len(result_3)
	num_gens.append(gens)

ax3.hist(num_gens)
ax3.set_title( "Times to Fixation" )
ax3.set_xlabel( "Generation") 
ax3.set_ylabel("Frequency") 

#Exercise 3
"""We can use our model to investigate how changing the population size 
affects the time to fixation. Pick at least five population sizes greater 
than or equal to 50. For each population size, run the model at least 50 times 
and find the average time to fixation. Keep your allele frequency constant 
for all runs. Create a scatter or line plot of population size vs. average time 
to fixation.

We can do the same for allele frequencies. This time, pick a population size 
and vary the allele frequency. Run at least 10 trials for each allele frequency. 
If your this takes a while to run, decrease your population size. For me, 
1000 individuals and 10 trials per allele frequency ran fast enough."""

pop_sizes={50:[],100:[],150:[],200:[],250:[]}

avg_time=[]

for q in pop_sizes.keys():
	for h in range(50):
		result_3=pop_dyn(0.5,q)
	avg_time.append(len(result_3))


ax4.plot(pop_sizes.keys(), avg_time)
ax4.set_title( "Population Size and Fixation" )
ax4.set_xlabel( "Population Size") 
ax4.set_ylabel("Average Time to Fixation") 

#now do allele freq variation instead

freq={0.1:[],0.2:[],0.3:[],0.4:[],0.5:[],0.6:[],0.7:[],0.8:[],0.9:[]}

avg_time_2=[]

for l in freq.keys():
	for k in range(10):
		result_4=pop_dyn(l,100)
	avg_time_2.append(len(result_4))

ax5.plot(freq.keys(), avg_time_2)
ax5.set_title( "Allele Frequency and Fixation" )
ax5.set_xlabel( "Allele Frequency") 
ax5.set_ylabel("Average Time to Fixation") 

plt.tight_layout()
plt.show()

#Exercise 4: Interpreting Data

"""Answer one of the two questions below 3 times 
(any combination works - you can do 3 plots, 1 plot and 2 assumptions, etc.).
For any plot, explain the results you see. What might be contributing to it? 
What does it mean biologically?
For any assumption in the Wright-Fisher model, 
how might changing that assumption affect the result? 
How might nature and biology violate these assumptions?"""

#For the first plot, allele frequency
"""Consider the assumption that everyone reproduces once per generation.
In nature this is false. If one pair with allele A had 10 offspring 
compared to a pair who had different alleles (allele B) who had 1 offspring, 
then this could affect time to allele fixation. If this same pattern
occured over generations then this would lead to allele A 
reaching fixation sooner"""

#Looking at the plot of allele frequency vs time to fixation
"""Biologically speaking, it makes sense that time to fixation peaks when an
allele has a starting frequency around 0.5 because it is the farthest to 
fixation (ie 0 or 1). As frequency gets closer to 0 or 1, average time to
fixation goes down. This makes sense since alleles closer to fixation will
by definition on the whole reach fixation sooner."""

#Looking at the plot of population time vs fixation
"""The overall trend appears to be that a larger population takes longer
to reach fixation. This makes sense because there will be more individuals
propogating different alleles and when there are more "undesired" (aka not
what we are aiming to get to fixation) alleles it will take longer for them
to be overrun through generations"""












