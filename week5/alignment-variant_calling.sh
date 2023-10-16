#!/bin/bash

#bwa index sacCer3.fa

#format of sample is A01_09.fastq

#for sample in 09 11 23 24 27 31 35 39 62 63
#do
	#echo "Aligning sample:" $sample
	#bwa mem -t 4 -R "@RG\tID:${sample}\tSM:${sample}" \
	#sacCer3.fa A01_${sample}.fastq > ${sample}.sam

	#samtools sort -O bam -o ${sample}.bam ${sample}.sam

	#samtools index ${sample}.bam
	
#done

#freebayes -f sacCer3.fa -p 2 --genotype-qualities 09.bam 11.bam 23.bam 24.bam 27.bam 31.bam 35.bam 39.bam 62.bam 63.bam> var.vcf

#vcffilter -f "QUAL>20" var.vcf > filtered_var.vcf

#vcfallelicprimitives -k -g filtered_var.vcf > decomposed_var.vcf

#snpEff download R64-1-1.105

#snpEff ann R64-1-1.105 decomposed_var.vcf > annotated_var.vcf

#head -n 100 annotated_var.vcf > head_var.vcf