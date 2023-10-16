#!/bin/python

import matplotlib.pyplot as plt

read_depth_DP=[]
genotype_quality_GQ=[]
allele_frequency_AF=[]
predicted_muts=[]

#not sure how to get predicted effects

for line in open("head_var.vcf"):
    if line.startswith('#'):
        continue
    fields=[]
    fields = line.rstrip('\n').split('\t')
    samples=fields[9:]
    for sample in range(len(samples)):
    	split_sample=samples[sample].split(":")
    	if split_sample[0] == ".":
    		continue
    	read_depth_DP.append(float(split_sample[2]))
    	genotype_quality_GQ.append(float(split_sample[1]))
    info=fields[7]
    split_info=info.split(";")
    allele=split_info[3]
    AF=allele.split("=")
    allele_frequency_AF.append(float(AF[1]))
    predict_mut=split_info[-2]
    predicted_muts.append(predict_mut)

effects_dict={"count_snp":0,"count_del":0}


for value in range(len(predicted_muts)):
	if predicted_muts[value]=="TYPE=snp":
		effects_dict["count_snp"]+=1
	elif predicted_muts[value]=="TYPE=del":
		effects_dict["count_del"]+=1



fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2)

ax1.hist(read_depth_DP)
ax1.set_title( "Read Depth" ) 
ax1.set_xlabel("DP")
ax1.set_ylabel("Frequency")

ax2.hist(genotype_quality_GQ)
ax2.set_title( "Genotype Quality" ) 
ax2.set_xlabel("GQ")
ax2.set_ylabel("Frequency")

ax3.hist(allele_frequency_AF)
ax3.set_title( "Allele Frequency" ) 
ax3.set_xlabel("AF")
ax3.set_ylabel("Frequency")

ax4.bar(list(effects_dict.keys()), list(effects_dict.values()))
ax4.set_title( "Predicted Effects" ) 
ax4.set_xlabel("Mutation Type")
ax4.set_ylabel("Frequency")

plt.tight_layout()
fig.savefig( "variation.png" )
#plt.show()
#plt.close( fig )"""