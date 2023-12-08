#!/usr/bin/env python

import sys
import scanpy as sc
import numpy as np
import matplotlib.pyplot as plt

# Read the 10x dataset filtered down to just the highly-variable genes
adata = sc.read_h5ad("variable_data.h5")
adata.uns['log1p']['base'] = None # This is needed due to a bug in scanpy 

sc.pp.neighbors(adata, n_neighbors=10, n_pcs=40)
sc.tl.leiden(adata)

sc.tl.umap(adata,maxiter=900)
sc.tl.tsne(adata)

fig, axes = plt.subplots(ncols=2)

sc.pl.umap(adata, color=['leiden'], ax = axes[0], title="UMAP", show=False)
sc.pl.tsne(adata, color=['leiden'], ax = axes[1], title="tSNE", show=False)

plt.tight_layout()
plt.savefig("fig1.png")

wilcoxon_adata=sc.tl.rank_genes_groups(adata, groupby='leiden', method='wilcoxon', use_raw=True, copy=True)
logreg_adata=sc.tl.rank_genes_groups(adata, groupby='leiden', method='logreg', use_raw=True, copy=True)

fig, axes = plt.subplots()

sc.pl.rank_genes_groups(wilcoxon_adata, ax = axes, title="Wilcoxon", n_genes=25, sharey=False, show=False, use_raw=True)
sc.pl.rank_genes_groups(logreg_adata, ax = axes, title="Log Reg", n_genes=25, sharey=False, show=False, use_raw=True)

plt.savefig("fig2wilcoxon.png")
plt.savefig("fig2logreg.png")

leiden = adata.obs['leiden']
umap = adata.obsm['X_umap']
tsne = adata.obsm['X_tsne']
adata = sc.read_h5ad('filtered_data.h5')
adata.obs['leiden'] = leiden
adata.obsm['X_umap'] = umap
adata.obsm['X_tsne'] = tsne

adata.write('filtered_clustered_data.h5')







