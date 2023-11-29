#!/usr/bin/env python

import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats import multitest
from pydeseq2 import preprocessing
from pydeseq2.dds import DeseqDataSet
from pydeseq2.ds import DeseqStats
import matplotlib.pyplot as plt

# read in data
counts_df = pd.read_csv("gtex_whole_blood_counts_formatted.txt", index_col = 0)

# read in metadata
metadata = pd.read_csv("gtex_metadata.txt", index_col = 0)

counts_df_normed = preprocessing.deseq2_norm(counts_df)[0]
counts_df_normed = np.log2(counts_df_normed + 1)
full_design_df = pd.concat([counts_df_normed, metadata], axis=1)
model = smf.ols(formula = 'Q("DDX11L1") ~ SEX', data=full_design_df)
results = model.fit()
slope = results.params[1]
pval = results.pvalues[1]

regression_df=pd.DataFrame(columns=["Gene", "Slope", "Pval"])

column_names=counts_df_normed.columns

for column in column_names:
	model=smf.ols(formula= 'Q(column) ~ SEX', data=full_design_df)
	results=model.fit()
	slope=results.params[1]
	pval=results.pvalues[1]
	new_row={"Gene": column, "Slope": slope, "Pval": pval}
	regression_df.loc[len(regression_df.index)] = [column, slope, pval]

regression_df.to_csv("regression.csv", index=False)

regression_read_df=pd.read_csv("regression.csv", index_col=0)

pvals_list=regression_read_df["Pval"]

reject, corrected_pvals=multitest.fdrcorrection(pvals_list, alpha=0.1)

fdr_corrections_df=pd.DataFrame({"Original_pvals":pvals_list,"Reject":reject,"Corrected_pvals":corrected_pvals})

fdr_corrections_df['Corrected_pvals'] = fdr_corrections_df['Corrected_pvals'].fillna(1.0)

fdr10_rows= fdr_corrections_df.loc[:,'Reject']==True
fdr10_df=fdr_corrections_df.loc[fdr10_rows] 

fdr10_gene_list = fdr10_df.index.tolist()

f=open("fdr10_1.5.txt", "a")

for item in range(len(fdr10_gene_list)):
	f.write(fdr10_gene_list[item]+',')

dds = DeseqDataSet(
    counts=counts_df,
    metadata=metadata,
    design_factors="SEX",
    n_cpus=4,)

dds.deseq2()
stat_res = DeseqStats(dds)
stat_res.summary()
results = stat_res.results_df

results.to_csv("results.csv", index=True)
results=pd.read_csv("results.csv", index_col=0)

fdr10_rows_dseq= results.loc[:,'padj']< 0.1
fdr10_dseq_df=results.loc[fdr10_rows_dseq] 

fdr10_dseq_gene_list = fdr10_dseq_df.index.tolist()

g=open("fdr10_2.txt", "a")

for item in range(len(fdr10_dseq_gene_list)):
	g.write(fdr10_dseq_gene_list[item]+',')

fdr10_1_set=set(fdr10_gene_list)
fdr10_2_set=set(fdr10_dseq_gene_list)

genes_1=0
genes_2=0
genes_both=0

for value in range(len(fdr10_gene_list)):
	if fdr10_gene_list[value] in fdr10_2_set:
		genes_both+=1
	elif fdr10_gene_list[value] not in fdr10_2_set:
		genes_1+=1

for value in range(len(fdr10_dseq_gene_list)):
	if fdr10_dseq_gene_list[value] not in fdr10_1_set:
		genes_2+=1

jaccard_index=genes_both/(genes_1+genes_2)*100

print(jaccard_index)


fdr10_log2_rows=fdr10_dseq_df.loc[:,'log2FoldChange']>1
fdr10_log2_df=fdr10_dseq_df.loc[fdr10_log2_rows]

fdr10_log2_xvals=fdr10_log2_df.loc[:,'log2FoldChange'].tolist()
fdr10_log2_yvals_plain=fdr10_log2_df.loc[:,'padj'].tolist()

fdr10_log2_yvals=[]
for value in range(len(fdr10_log2_yvals_plain)):
	fdr10_log2_yvals.append(-np.log10(fdr10_log2_yvals_plain[value]))

x_vals=results.loc[:,'log2FoldChange'].tolist()
y_vals_plain=results.loc[:,'padj'].tolist()

y_vals=[]
for value in range(len(y_vals_plain)):
	y_vals.append(-np.log10(y_vals_plain[value]))

fig, ax= plt.subplots(1,1)

ax.scatter(x_vals,y_vals,c="blue")
ax.scatter(fdr10_log2_xvals,fdr10_log2_yvals,c="red")

ax.set_title("Differential Expression")
ax.set_xlabel("log2FoldChange")
ax.set_ylabel("-log10(padj)")

plt.tight_layout()
plt.savefig("volcano_plot.png")













