Step 1,1:

Rscript runChicago.R --design-dir raw/Design --en-feat-list raw/Features/featuresGM.txt --export-format washU_text raw/PCHIC_Data/GM_rep1.chinput,raw/PCHIC_Data/GM_rep2.chinput,raw/PCHIC_Data/GM_rep3.chinput output

Step 1.2:
CTCF has ~3 fold enrichment of meaningful interactions, H3K4me1 has ~2.5 fold, H3K4me3 has ~3 fold, H3K27ac has ~2.5, H3K9me3 has ~2 fold, H3K27me3 has no difference between meaningful and random interactions. It is interesting that H3K27me3 has a similar amount of random interactions to significant interactions. Perhaps this is because H3K27me3 tends to spread over repressed regions.

Step 2.2:

promoter-promoter
['chr20', '17660712', '17951709', '.', '973', '33.85', '.', '0', 'chr20', '17946510', '17951709', 'MGME1;SNX5', '+', 'chr20', '17660712', '17672229', 'RRBP1', '+']
['chr20', '24972345', '25043735', '.', '973', '33.84', '.', '0', 'chr20', '24972345', '24985047', 'APMAP', '+', 'chr20', '25036380', '25043735', 'ACSS1', '+']
['chr20', '44438565', '44565593', '.', '1000', '34.77', '.', '0', 'chr20', '44562442', '44565593', 'PCIF1', '+', 'chr20', '44438565', '44442365', 'UBE2C', '+']
['chr20', '44452862', '44565593', '.', '974', '33.89', '.', '0', 'chr20', '44562442', '44565593', 'PCIF1', '+', 'chr20', '44452862', '44471524', 'SNX21;TNNC2', '+']
['chr20', '44438565', '44607204', '.', '986', '34.29', '.', '0', 'chr20', '44596299', '44607204', 'FTLP1;ZNF335', '+', 'chr20', '44438565', '44442365', 'UBE2C', '+']
['chr21', '26837918', '26939577', '.', '978', '34.02', '.', '0', 'chr21', '26837918', '26842640', 'snoU13', '+', 'chr21', '26926437', '26939577', 'MIR155HG', '+']

promoter-enhancer
['chr20', '5585992', '5628028', '.', '830', '28.88', '.', '0', 'chr20', '5585992', '5601172', 'GPCPD1', '+', 'chr20', '5625693', '5628028', '.', '-']
['chr20', '5515866', '5933156', '.', '750', '26.08', '.', '0', 'chr20', '5929472', '5933156', 'MCM8;TRMT6', '+', 'chr20', '5515866', '5523933', '.', '-']
['chr20', '55957140', '56074932', '.', '928', '32.29', '.', '0', 'chr20', '55957140', '55973022', 'RBM38;RP4-800J21.3', '+', 'chr20', '56067414', '56074932', '.', '-']
['chr21', '26790966', '26939577', '.', '838', '29.17', '.', '0', 'chr21', '26926437', '26939577', 'MIR155HG', '+', 'chr21', '26790966', '26793953', '.', '-']
['chr21', '26793954', '26939577', '.', '754', '26.23', '.', '0', 'chr21', '26926437', '26939577', 'MIR155HG', '+', 'chr21', '26793954', '26795680', '.', '-']
['chr21', '26797667', '26939577', '.', '952', '33.13', '.', '0', 'chr21', '26926437', '26939577', 'MIR155HG', '+', 'chr21', '26797667', '26799364', '.', '-']

Step 2.3: Does it make sense for this gene to be interacting with enhancers in GM12878? Explain.

Image 1 depicts GPCPD1(glycerophosphocholine phosphodiesterase 1) which enables glycerophosphocholine phosphodiesterase activity and is involved in glycerophospholipid catabolic process. It make sense that this gene would interact with enhancers. Image 2 depicts ZNF337(zinc finger protein 337) which has many different isoforms from alternative splicing.







