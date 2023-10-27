#!/usr/bin/env python

import sys
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
import pandas as pd

eigenvec_data = pd.read_csv('pcaresults.eigenvec', sep=' ', header=None)

pca1=list(eigenvec_data.loc[:,2])
pca2=list(eigenvec_data.loc[:,3])

#print(pca1)
#print(pca2)

fig, ax1=plt.subplots()
ax1.scatter(pca1,pca2)

ax1.set_title( "Generic Relatedness" ) 
ax1.set_ylabel( "pca2") 
ax1.set_xlabel("pca1") 

plt.tight_layout()
fig.savefig( "ex1_2.png")
#plt.show()


allele_freq_data=pd.read_csv('allele_frequencies.frq', delim_whitespace=True)

#print(allele_freq_data)

allele_freq=list(allele_freq_data.loc[:,"MAF"])

#print(allele_freq)

fig, ax2 =plt.subplots()
ax2.hist(allele_freq, bins=80)

ax2.set_title( "Allele Frequencies" ) 
ax2.set_ylabel( "Frequency") 
ax2.set_xlabel("Allele Frequency") 

plt.tight_layout()
fig.savefig( "ex2_2.png")
#plt.show()

GS451_data=pd.read_csv('phenotype_gwas_results_GS451.assoc.linear', delim_whitespace=True)
CB1908_data=pd.read_csv('phenotype_gwas_results_CB1908.assoc.linear', delim_whitespace=True)

#print(GS451_data)
#print(CB1908_data)

x_values=GS451_data.index.values.tolist()

GS451_p_vals=list(GS451_data.loc[:,"P"])
GS451_p_vals_converted=list(-(np.log10(GS451_p_vals)))

CB1908_p_vals=list(CB1908_data.loc[:,"P"])
CB1908_p_vals_converted=list(-(np.log10(CB1908_p_vals)))

"""color_G_list=[]
for item in GS451_p_vals_converted:
	if item >5:
		color_G_list.append("Red")
	else:
		color_G_list.append("Blue")

color_C_list=[]
for item in CB1908_p_vals_converted:
	if item >5:
		color_C_list.append("Red")
	else:
		color_C_list.append("Blue")

fig, (ax3, ax4) = plt.subplots(1,2)

ax3.scatter(x_values,GS451_p_vals_converted, c=color_G_list)
ax3.set_title( "GGS451 Manhattan Plot" ) 
ax3.set_ylabel( "-log10(P)")
ax3.set_ylim(0,10) 
ax3.set_xlabel("Position") 

ax4.scatter(x_values,CB1908_p_vals_converted, c=color_C_list)
ax4.set_title( "CB1908 Manhattan Plot" ) 
ax4.set_ylabel( "-log10(P)") 
ax4.set_ylim(0,10) 
ax4.set_xlabel("Position") 

plt.tight_layout()
fig.savefig( "ex3_2.png")
#plt.show()"""

#max_GS451=np.max(GS451_p_vals_converted)

#index_max=np.where(GS451_p_vals_converted==max_GS451)

min_row_GS451=GS451_data.loc[GS451_data["P"].idxmin()]

effect_size_data=pd.read_csv('rs7257475_genotypes.raw', delim_whitespace=True)

GS451_IC50_data=pd.read_csv('GS451_IC50.txt', delim_whitespace=True)

all_data=pd.concat([effect_size_data,GS451_IC50_data],axis=1,join="inner")
 
rows_0=all_data.loc[:,"rs7257475_T"]== 0.0
data_0=all_data.loc[rows_0,:] 
IC50_0_list=list(data_0.loc[:,"GS451_IC50"])

IC50_0_fixed_list=IC50_0_list[:16]+IC50_0_list[17:]

IC50_0=np.array(IC50_0_fixed_list)

rows_1=all_data.loc[:,"rs7257475_T"]== 1.0
data_1=all_data.loc[rows_1,:] 
IC50_1=np.array(data_1.loc[:,"GS451_IC50"])

rows_2=all_data.loc[:,"rs7257475_T"]== 2.0
data_2=all_data.loc[rows_2,:] 
IC50_2=np.array(data_2.loc[:,"GS451_IC50"])

all_IC50=[IC50_0,IC50_1,IC50_2]
labels=["0","1","2"]

fig, ax5=plt.subplots()
ax5.boxplot(all_IC50,labels=labels)
ax5.set_title( "Effect Size" ) 
ax5.set_ylabel( "GS451_IC50 (Phenotype)") 
ax5.set_ylim(0,15) 
ax5.set_xlabel("Genotype") 
plt.tight_layout()
fig.savefig( "ex3_3.png")
#plt.show()

min_row_CB1908=CB1908_data.loc[CB1908_data["P"].idxmin()]
print(min_row_GS451)


