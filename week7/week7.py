#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt
import numpy as np

def main():
    # Load file names from command line
    ONT_fname, bisulfite_fname, out_fname, norm_ONT, norm_bisulfite, tum_ONT, tum_bisulfite = sys.argv[1:8]
    ONT= load_data(ONT_fname)
    bisulfite= load_data(bisulfite_fname)

    normal_ONT= load_data(norm_ONT)
    normal_bisulfite=load_data(norm_bisulfite)
    tumor_ONT= load_data(tum_ONT)
    tumor_bisulfite=load_data(tum_bisulfite)

    ONT_list=[]
    bisulfite_list=[]

    normal_ONT_list=[]
    normal_bisulfite_list=[]
    tumor_ONT_list=[]
    tumor_bisulfite_list=[]

    find_meth_sites(ONT,ONT_list)
    find_meth_sites(bisulfite,bisulfite_list)

    find_meth_sites(normal_ONT, normal_ONT_list)
    find_meth_sites(normal_bisulfite, normal_bisulfite_list)
    find_meth_sites(tumor_ONT, tumor_ONT_list)
    find_meth_sites(tumor_bisulfite, tumor_bisulfite_list)

    ONT_pos_set=set()
    bisulfite_pos_set=set()

    normal_ONT_pos_set=set()
    normal_bisulfite_pos_set=set()
    tumor_ONT_pos_set=set()
    tumor_bisulfite_pos_set=set()

    make_pos_list(ONT_list, ONT_pos_set)
    make_pos_list(bisulfite_list, bisulfite_pos_set)

    make_pos_list(normal_ONT_list, normal_ONT_pos_set)
    make_pos_list(normal_bisulfite_list, normal_bisulfite_pos_set)
    make_pos_list(tumor_ONT_list, tumor_ONT_pos_set)
    make_pos_list(tumor_bisulfite_list, tumor_bisulfite_pos_set)

    ONT_unique=set()
    bisulfite_unique=set()
    ONT_bisulfite_shared=set()

    normal_ONT_unique=set()
    normal_bisulfite_unique=set()
    tumor_ONT_unique=set()
    tumor_bisulfite_unique=set()
    ONT_normal_tumor_shared=set()
    bisulfite_normal_tumor_shared=set()

    find_unique_multi_sets(ONT_list, bisulfite_pos_set, ONT_unique, ONT_bisulfite_shared)
    find_unique_multi_sets(bisulfite_list, ONT_pos_set, bisulfite_unique, ONT_bisulfite_shared)

    find_unique_multi_sets(normal_ONT_list, tumor_ONT_pos_set, normal_ONT_unique, ONT_normal_tumor_shared)
    find_unique_multi_sets(normal_bisulfite_list, tumor_bisulfite_pos_set, normal_bisulfite_unique, bisulfite_normal_tumor_shared)
    find_unique_multi_sets(tumor_ONT_list, normal_ONT_pos_set, tumor_ONT_unique, ONT_normal_tumor_shared)
    find_unique_multi_sets(tumor_bisulfite_list, normal_bisulfite_pos_set, tumor_bisulfite_unique, bisulfite_normal_tumor_shared)


    ONT_unique_amount= len(ONT_unique)
    bisulfite_unique_amount=len(bisulfite_unique)
    ONT_bisulfite_shared_amount= len(ONT_bisulfite_shared)
    total_site= ONT_unique_amount + bisulfite_unique_amount + ONT_bisulfite_shared_amount

    ONT_percent= ONT_unique_amount / total_site * 100
    bisulfite_percent= bisulfite_unique_amount / total_site * 100
    shared_percent= ONT_bisulfite_shared_amount / total_site * 100

    print(ONT_percent, bisulfite_percent, shared_percent)

    ONT_coverage=[]
    bisulfite_coverage=[]

    make_list_coverages(ONT, ONT_coverage)
    make_list_coverages(bisulfite, bisulfite_coverage)

    ONT_shared_meth_scores=[]
    bisulfite_shared_meth_scores=[]

    make_list_shared_meth_scores(ONT, ONT_shared_meth_scores, ONT_bisulfite_shared)
    make_list_shared_meth_scores(bisulfite, bisulfite_shared_meth_scores, ONT_bisulfite_shared)

    normal_ONT_meth_scores=[]
    normal_bisulfite_meth_scores=[]
    tumor_ONT_meth_scores=[]
    tumor_bisulfite_meth_scores=[]

    make_list_shared_meth_scores(normal_ONT, normal_ONT_meth_scores, ONT_normal_tumor_shared)
    make_list_shared_meth_scores(normal_bisulfite, normal_bisulfite_meth_scores, bisulfite_normal_tumor_shared)
    make_list_shared_meth_scores(tumor_ONT, tumor_ONT_meth_scores, ONT_normal_tumor_shared)
    make_list_shared_meth_scores(tumor_bisulfite, tumor_bisulfite_meth_scores, bisulfite_normal_tumor_shared)

    norm_ONT_meth_mod=[]
    norm_bis_meth_mod=[]
    tum_ONT_meth_mod=[]
    tum_bis_meth_mod=[]

    mod_make_list_shared_meth_scores(normal_ONT, norm_ONT_meth_mod, ONT_normal_tumor_shared, bisulfite_normal_tumor_shared)
    mod_make_list_shared_meth_scores(normal_bisulfite, norm_bis_meth_mod, ONT_normal_tumor_shared, bisulfite_normal_tumor_shared)
    mod_make_list_shared_meth_scores(tumor_ONT, tum_ONT_meth_mod, ONT_normal_tumor_shared, bisulfite_normal_tumor_shared)
    mod_make_list_shared_meth_scores(tumor_bisulfite, tum_bis_meth_mod, ONT_normal_tumor_shared, bisulfite_normal_tumor_shared)

    ONT_normal_tumor_meth_diff=[]
    bisulfite_normal_tumor_meth_diff=[]

    substract_lists(normal_ONT_meth_scores, tumor_ONT_meth_scores, ONT_normal_tumor_meth_diff)
    substract_lists(normal_bisulfite_meth_scores, tumor_bisulfite_meth_scores, bisulfite_normal_tumor_meth_diff)

    ONT_shared_diff=[]
    bis_shared_diff=[]

    substract_lists(norm_ONT_meth_mod, tum_ONT_meth_mod, ONT_shared_diff)
    substract_lists(norm_bis_meth_mod, tum_bis_meth_mod, bis_shared_diff)
    Rcoeff_2=np.corrcoef(ONT_shared_diff, bis_shared_diff)


    ONT_diff_final=[]
    bisulfite_diff_final=[]

    exclude_zeros_from_list(ONT_normal_tumor_meth_diff, ONT_diff_final)
    exclude_zeros_from_list(bisulfite_normal_tumor_meth_diff, bisulfite_diff_final)


    fig, ax= plt.subplots(3,1, figsize=(10,10))

    ax[0].hist(ONT_coverage, label="Nanopore (ONT)", alpha=0.3, bins=1000)
    ax[0].hist(bisulfite_coverage, label= "Bisulfite", alpha=0.3, bins=1000)
    ax[0].set_title("Coverage")
    ax[0].set_xlim(0,125)
    ax[0].set_xlabel("Coverage")
    ax[0].legend()

    H, xedges, yedges=np.histogram2d(ONT_shared_meth_scores, bisulfite_shared_meth_scores, bins=(100,100))
    Rcoeff=np.corrcoef(ONT_shared_meth_scores, bisulfite_shared_meth_scores)

    ax[1].imshow(np.log10(H + 1 ))
    ax[1].set_title(f"Methylation Scores R={round(Rcoeff[0,1],3)}")

    ax[2].violinplot([ONT_diff_final, bisulfite_diff_final])
    ax[2].set_title(f"Methylation Changes R={round(Rcoeff_2[0,1],3)}")
    ax[2].set_xticks([1,2], labels=["ONT", "Bisulfite"])

    plt.tight_layout()
    plt.savefig(out_fname)


def load_data(fname):
    data= []
    for line in open(fname):
        line= line.rstrip().split()
        data.append([line[0],int(line[1]),int(line[2]), float(line[3]), int(line[4])])
    return data

def find_meth_sites(data,output_list):
	for i in range(len(data)):
		if data[i][3] != 0:
			output_list.append(data[i])

def make_pos_list(input_list, output_set):
	for i in range(len(input_list)):
		output_set.add(input_list[i][1])

def find_unique_multi_sets(input_list_1, input_set_2, output_1_unique, output_both):
	for i in range(len(input_list_1)):
		if input_list_1[i][1] not in input_set_2:
			output_1_unique.add(input_list_1[i][1])
		elif input_list_1[i][1] not in output_both:
			output_both.add(input_list_1[i][1])

def make_list_coverages(input_list, output_list):
	for i in range(len(input_list)):
		output_list.append(input_list[i][4])

def make_list_shared_meth_scores(input_list, output_list, set_to_check):
	for i in range(len(input_list)):
		if input_list[i][1] in set_to_check:
			output_list.append(input_list[i][3])

def mod_make_list_shared_meth_scores(input_list, output_list, set_1, set_2):
	for i in range(len(input_list)):
		if input_list[i][1] in set_1 and set_2:
			output_list.append(input_list[i][3])

def exclude_zeros_from_list(input_list, output_list):
	for i in range(len(input_list)):
		if input_list[i] != 0:
			output_list.append(input_list[i])

def substract_lists(list_1, list_2, output_list):
	for i in range(len(list_1)):
		output_list.append(list_1[i]-list_2[i])


main()