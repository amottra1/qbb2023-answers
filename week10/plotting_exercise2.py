#!/usr/bin/env python

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

bob_ross_df=pd.read_csv("bob_ross.csv")

#look at use of certain color over time 
#line plot season num vs % of paintings in that season that use the color

green_rows=bob_ross_df.loc[:,"Phthalo_Green"] == True
green_df=bob_ross_df.loc[green_rows,"season"]
green_seasons=green_df.loc[:].tolist()

seasons=[]
green_uses=[]
for i in range(32):
	if i != 0:
		seasons.append(i)
		green_use=green_seasons.count(i)
		green_uses.append(green_use/13*100)

fig1, ax1= plt.subplots(1,1)
ax1.plot(seasons, green_uses, color="green")
ax1.set_title("Use of Phthalo Green")
ax1.set_xlabel("Season")
ax1.set_ylabel("% Paintings with Phthalo Green")

plt.tight_layout()
plt.savefig("2.1.png")

#look at warm vs cool colors used over time
#line plot num colors(y) vs episode num in season (x)
#exclude black, white and clear

warm_colors=["Bright Red", "Burnt Umber", "Cadmium Yellow", "Dark Sienna", "Indian Red", "Indian Yellow", "Van Dyke Brown", "Yellow Ochre", "Alizarin Crimson"]
cool_colors=["Phthalo Blue", "Phthalo Green", "Prussian Blue", "Sap Green"]

warm_colors_set=set(warm_colors)
cool_colors_set=set(cool_colors)

num_warm=len(warm_colors)
num_cool=len(cool_colors)

color_list=bob_ross_df.loc[:,"colors"].tolist()

#items are in order by season then episode so just use index as measure of timepoint
index_list=bob_ross_df.index.tolist()

formatted_color_list=[]

for item in color_list:
	item_list=[]
	list_1=item.split("'")
	list2=[]
	for item1 in list_1:
		if len(item1)>3:
			list2.append(item1)
	for item2 in list2:
		list2a=item2.split("\\")
		for item2a in list2a:
			if len(item2a) > 3:
				item_list.append(item2a)
	formatted_color_list.append(item_list)

warm_num=[]
cool_num=[]

for val in formatted_color_list:
	warm=0
	cool=0
	for color in val:
		if color in warm_colors_set:
			warm+=1
		elif color in cool_colors_set:
			cool+=1
	warm_num.append(warm/num_warm)
	cool_num.append(cool/num_cool)


avg1=sum(warm_num[0:78])/78
avg2=sum(warm_num[78:156])/78
avg3=sum(warm_num[156:234])/78
avg4=sum(warm_num[234:312])/78
avg5=sum(warm_num[312:])/91

cavg1=sum(cool_num[0:78])/78
cavg2=sum(cool_num[78:156])/78
cavg3=sum(cool_num[156:234])/78
cavg4=sum(cool_num[234:312])/78
cavg5=sum(cool_num[312:])/91


warm_num_avgs=[avg1, avg2, avg3, avg4, avg5]
cool_num_avgs=[cavg1, cavg2, cavg3, cavg4, cavg5]

time=["1-6", "7-12", "13-18", "19-24", "25-31"]

fig3,ax3 = plt.subplots(1,1)
ax3.bar(time,warm_num_avgs,width=+0.35,align="edge",label="Warm Colors", color="red")
ax3.bar(time, cool_num_avgs, width=-0.35,align="edge", label="Cool Colors", color="blue")
ax3.set_title("Warm and Cool Color Use Over Time")
ax3.set_xlabel("Time (Season Range")
ax3.set_ylabel("Number of Colors Used")

plt.legend()
plt.tight_layout()
plt.savefig("2.3.png")

#colors used in painting
#histogram of num_colors used

num_colors=bob_ross_df.loc[:,"num_colors"].tolist()

fig2,ax2 = plt.subplots(1,1)
ax2.hist(num_colors,14)
ax2.set_title("Number of Unqiue Colors Used")
ax2.set_xlabel("Number of Colors")
ax2.set_ylabel("Frequency")

plt.tight_layout()
plt.savefig("2.2.png")







