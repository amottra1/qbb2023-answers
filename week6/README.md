Step 1.1: 

plink --vcf genotypes.vcf --recode --out ped_map_myfile
plink --file ped_map_myfile --pca 10 --out pcaresults


Step 2.1:

plink --file ped_map_myfile --freq --out allele_frequencies

Step 3.1:

plink --vcf genotypes.vcf --linear --pheno GS451_IC50.txt --covar pcaresults.eigenvec --allow-no-sex --out phenotype_gwas_results_GS451

plink --vcf genotypes.vcf --linear --pheno CB1908_IC50.txt --covar pcaresults.eigenvec --allow-no-sex --out phenotype_gwas_results_CB1908


Step 3.3:

plink --file ped_map_myfile --snp rs7257475 --recode A --out rs7257475_genotypes

Step 3.4:

Top hit for CB1908: Chr 12 BP  49190411
This is in the DIP2B gene. This gene is involved in methylation so likely disruptions could disrupt methylation of other genes directly contributing to low lymphocyte counts in mutated genotypes.

Top hit for GS451: Chr 19 BP 20372113
This is in the ZNF826 gene. This gene is likely involved in enabling DNA-binding transcription factor activity so disruptions could lead to disruptions of transcription of other genes directly contributing to the low lymphocyte counts in mutated genotypes.