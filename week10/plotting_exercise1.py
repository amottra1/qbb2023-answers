#!/usr/bin/env python

import numpy as np
import pandas as pd
from pydeseq2 import preprocessing
from matplotlib import pyplot as plt

"""# read in data
counts_df = pd.read_csv("gtex_whole_blood_counts_formatted.txt", index_col = 0)
# read in metadata
metadata = pd.read_csv("gtex_metadata.txt", index_col = 0)
# normalize
counts_df_normed = preprocessing.deseq2_norm(counts_df)[0]
# log
counts_df_logged = np.log2(counts_df_normed + 1)
# merge with metadata
full_design_df = pd.concat([counts_df_logged, metadata], axis=1)

full_design_df.to_csv("data_df", index=True)"""

data_df=pd.read_csv("data_df", index_col=0)

GTEX_df=data_df.loc["GTEX-113JC","DDX11L1":"MT-TP"]

genes_list=GTEX_df.index.tolist()
GTEX_exp_list=GTEX_df.loc[:].tolist()

genes_list_nonzero=[]
GTEX_exp_list_nonzero=[]
for i in range(len(genes_list)):
	if GTEX_exp_list[i] != 0:
		genes_list_nonzero.append(genes_list[i])
		GTEX_exp_list_nonzero.append(GTEX_exp_list[i])

fig1, ax1= plt.subplots(1,1)

ax1.hist(GTEX_exp_list_nonzero, 20)

ax1.set_title("GTEX-113JC Gene Expression")
ax1.set_xlabel("log2(Gene Expression)")
ax1.set_ylabel("Frequency")

plt.tight_layout()
plt.savefig("1.1.png")		

rows_1=data_df.loc[:,"SEX"] == 1
rows_2=data_df.loc[:,"SEX"] == 2

MXD4_1=data_df.loc[rows_1,"MXD4"]
MXD4_2=data_df.loc[rows_2,"MXD4"]

MXD4_1_vals=MXD4_1.loc[:].tolist()
MXD4_2_vals=MXD4_2.loc[:].tolist()

fig2, ax2= plt.subplots(1,1)

ax2.hist(MXD4_1, 20, color="blue", label="Male", alpha=0.5)
ax2.hist(MXD4_2, 20, color="green", label="Female", alpha=0.5)

ax2.set_title("MXD4 Gene Expression")
ax2.set_xlabel("log2(Gene Expression)")
ax2.set_ylabel("Frequency")

plt.legend()
plt.tight_layout()
plt.savefig("1.2.png")

def find_number_age(age_range):
	rows=data_df.loc[:,"AGE"]== age_range
	df=data_df.loc[rows,:]
	num_age_var=df.shape[0]
	return num_age_var

age_20=find_number_age("20-29")
age_30=find_number_age("30-39")
age_40=find_number_age("40-49")
age_50=find_number_age("50-59")
age_60=find_number_age("60-69")
age_70=find_number_age("70-79")
age_80=find_number_age("80-89")

fig3, ax3= plt.subplots(1,1)

ax3.bar(["20-29","30-39","40-49","50-59","60-69","70-79","80-89"],[age_20,age_30,age_40,age_50,age_60,age_70,age_80])
ax3.set_title("Age Distribution")
ax3.set_xlabel("Age Range")
ax3.set_ylabel("Number of Subjects")

plt.tight_layout()
plt.savefig("1.3.png")

def find_medians_by_sex(age_range):
	rows_age=data_df.loc[:,"AGE"]==age_range
	age_df=data_df.loc[rows_age,:]
	rows_male=age_df.loc[:,"SEX"] == 1
	rows_female=age_df.loc[:,"SEX"] == 2
	male_age_df=age_df.loc[rows_male,"LPXN"]
	female_age_df=age_df.loc[rows_female,"LPXN"]
	male_vals=male_age_df.loc[:].tolist()
	female_vals=female_age_df.loc[:].tolist()
	male_floats=[]
	female_floats=[]
	for val in range(len(male_vals)):
		male_floats.append(float(male_vals[val]))
	for val in range(len(female_vals)):
		female_floats.append(float(female_vals[val]))
	median_male=np.median(male_floats)
	median_female=np.median(female_floats)
	return median_male, median_female

m20,f20=find_medians_by_sex("20-29")
m30,f30=find_medians_by_sex("30-39")
m40,f40=find_medians_by_sex("40-49")
m50,f50=find_medians_by_sex("50-59")
m60,f60=find_medians_by_sex("60-69")
m70,f70=find_medians_by_sex("70-79")

age_ranges=["20-29","30-39","40-49","50-59","60-69","70-79","80-89"]
male_yvals=[m20,m30,m40,m50,m60,m70,0]
female_yvals=[f20,f30,f40,f50,f60,f70,0]

fig4, ax4= plt.subplots(1,1)

ax4.bar(age_ranges,male_yvals,width=+0.35,align="edge",label="Male",color="blue")
ax4.bar(age_ranges,female_yvals,width=-0.35,align="edge",label="Female",color="red")
ax4.set_title("Median LPXN Expression")
ax4.set_xlabel("Age Range")
ax4.set_ylabel("Median log2(gene expression)")

plt.legend()
plt.tight_layout()
plt.savefig("1.4.png")








