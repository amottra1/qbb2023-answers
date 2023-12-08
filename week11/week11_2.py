#!/usr/bin/env python

import sys
import scanpy as sc
import numpy as np
import matplotlib.pyplot as plt

adata = sc.read_h5ad("filtered_clustered_data.h5")
adata.uns['log1p']['base'] = None # This is needed due to a bug in scanpy 

#B cells, Megakaryocytes, CD14 Monocytes
marker_genes=["MS4A1","PPBP", "CD14"]

fig, axes = plt.subplots()
sc.pl.dotplot(adata, marker_genes, ax = axes, title="Marker Genes", groupby='leiden', show=False)

plt.tight_layout()
plt.savefig("fig3_2.png")

identified_clusters=["0", "CD14 Monocytes", "B Cells", "3", "4", "5", "6", "Megakaryocytes"]
adata.rename_categories("leiden", identified_clusters)

fig, axes = plt.subplots()
sc.pl.umap(adata, color=['leiden'], ax = axes, title="UMAP Clusters", show=False)

plt.tight_layout()
plt.savefig("fig3_3.png")