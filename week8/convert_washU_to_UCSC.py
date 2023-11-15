#!/usr/bin/env python

import sys

baitmap, WashU, output_bed = sys.argv[1:4]

baitmap_list=[]
baitmap_ref_list=[]
baitmap_gene_dict={}
k=open(baitmap)
for line in k:
	line= line.rstrip().split()
	baitmap_list.append(['chr'+line[0],int(line[1]),int(line[2]),line[4]])
	baitmap_ref_list.append(['chr'+line[0],int(line[1]),int(line[2])])
	baitmap_gene_dict['chr'+line[0],int(line[1]),int(line[2])]=line[4]

WashU_list=[]
WashU_scores=[]
f=open(WashU)
for line in f:
	line= line.rstrip().split()
	start=line[0].rstrip().split(',')
	end=line[1].rstrip().split(',')
	WashU_list.append([[start[0], int(start[1]), int(start[2])],[end[0],int(end[1]),int(end[2])],float(line[2])])
	WashU_scores.append(float(line[2]))

max_score=float(max(WashU_scores))

output_list=[]
for interaction in WashU_list:
	#1 chrom
	out1=str(interaction[0][0])
	#2 chrom start (lowest start)
	out2=str(min(interaction[0][1],interaction[1][1]))
	#3 chrom end (highest end)
	out3=str(max(interaction[0][2],interaction[1][2]))
	#4 name '.'
	out4='.'
	#5 score (strength/max*1000)
	out5=str(int(interaction[2]/max_score*1000))
	#6 strength
	out6=str(int(interaction[2]))
	#7 ex '.'
	out7='.'
	#8 color '0'
	out8='0'
	if interaction[0] in baitmap_ref_list:
		#9 bait chrom
		out9=str(interaction[0][0])
		#10 bait start
		out10=str(interaction[0][1])
		#11 bait end
		out11=str(interaction[0][2])
		#12 bait gene
		out12=baitmap_gene_dict[tuple(interaction[0])]
		#13 source strand '+' for bait
		out13='+'
		#14 target chrom
		out14=str(interaction[1][0])
		#15 target start
		out15=str(interaction[1][1])
		#16 target end
		out16=str(interaction[1][2])
		if interaction[1] in baitmap_ref_list:
			#17 target name (gene if bait '.' if not bait)
			out17=baitmap_gene_dict[tuple(interaction[1])]
			#18 target strand '+' for bait '-' for not bait
			out18='+'
		elif interaction[1] not in baitmap_ref_list:
			#17 target name (gene if bait '.' if not bait)
			out17='.'
			#18 target strand '+' for bait '-' for not bait
			out18='-'
	else:
		#9 bait chrom
		out9=str(interaction[1][0])
		#10 bait start
		out10=str(interaction[1][1])
		#11 bait end
		out11=str(interaction[1][2])
		#12 bait gene
		out12=baitmap_gene_dict[tuple(interaction[1])]
		#13 source strand '+' for bait
		out13='+'
		#14 target chrom
		out14=str(interaction[0][0])
		#15 target start
		out15=str(interaction[0][1])
		#16 target end
		out16=str(interaction[0][2])
		#17 target name (gene if bait '.' if not bait)
		out17='.'
		#18 target strand '+' for bait '-' for not bait
		out18='-'

	output_list.append([out1,out2,out3,out4,out5,out6,out7,out8,out9,out10,out11,out12,out13,out14,out15,out16,out17,out18])

#print(output_list)

g=open(output_bed, "a")
g.write('track type=interact name="pCHIC description="Chromatin interactions" useScore=on maxHeightPixels=200:100:50 visibility=full')

for item in output_list:
	tab_sep_line='\t'.join(item)
	g.write('\n'+ tab_sep_line)
		
#find top scoring 6 for bait-bait and bait-target

bait_bait_list=[]
bait_target_list=[]
for interaction in output_list:
	if interaction[12] and interaction[17] == '+':
		bait_bait_list.append(interaction)
	else:
		bait_target_list.append(interaction)

bait_bait_scores=[]
for value in bait_bait_list:
	bait_bait_scores.append(float(value[4]))
bait_target_scores=[]
for value in bait_target_list:
	bait_target_scores.append(float(value[4]))

top_6_bait_bait=sorted(bait_bait_scores,reverse=True)[:6]
top_6_bait_target_list=sorted(bait_target_scores,reverse=True)[:6]

print("promoter-promoter")
for value in bait_bait_list:
	if float(value[4]) in top_6_bait_bait:
		print(value)

print("promoter-enhancer")
for value in bait_target_list:
	if float(value[4]) in top_6_bait_target_list:
		print(value)







