#!usr/bin/env python

import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import scipy.stats as sps
import statsmodels.api as sm

#Exercise 1

#Step 1.1
#You’ll start by exploring the data in aau1043_dnm.csv. 
#First, load this data into a pandas dataframe.

dnm=pd.read_csv("aau1043_dnm.csv")

#print(dnm)

#Step 1.2
"""You first want to count the number of paternally and maternally inherited DNMs 
in each proband. Using this dataframe, create a dictionary where the keys are the proband 
IDs and the value associated with each key is a list of length 2, where the first element 
in the list is the number of maternally inherited DNMs and the second element in the list 
is the number of paternally inherited DNMs for that proband. You can ignore DNMs without 
a specified parent of origin."""

my_dictionary={"":[]}


mat_rows=dnm.loc[:,"Phase_combined"]== "mother"
pat_rows=dnm.loc[:,"Phase_combined"]== "father"

mat_data=dnm.loc[mat_rows,:] #all data for rows that are maternal
pat_data=dnm.loc[pat_rows,:] #all data for rows that are paternal

#make list of pro IDs with no repeats

pro_id_total=list(dnm.loc[:,"Proband_id"])

#print(pro_id_total)

for i in pro_id_total:
	if i not in my_dictionary.keys():
		my_dictionary[i]=[0,0]

#check to make sure no rpelicates in keys
#print(len(my_dictionary.keys()))

#print(my_dictionary[5410])
for n in mat_data.loc[:,"Proband_id"]:
	my_dictionary[n][0]+=1

for k in pat_data.loc[:,"Proband_id"]:
	my_dictionary[k][1]+=1

#print(my_dictionary)

#Step 1.3

"""Step 1.3

Use the following code snippet to convert this dictionary into a new pandas dataframe 
(this assumes your dictionary from step 1.2 is called deNovoCount):

deNovoCountDF = pd.DataFrame.from_dict(deNovoCount, orient = 'index', 
columns = ['maternal_dnm', 'paternal_dnm'])"""

my_df=pd.DataFrame.from_dict(my_dictionary, orient="index",columns=['maternal_dnm','paternal_dnm'])

#print(my_df)

#Step 1.4

#Now, load the data from aau1043_parental_age.csv into a new pandas dataframe.

age=pd.read_csv("aau1043_parental_age.csv",
	index_col='Proband_id')

#print(age)

#Step 1.5

"""You now have two dataframes with complementary information. It would be nice to have 
all of this in one data structure. Use the pd.concat() function (more here) to 
combine your dataframe from step 3 with the dataframe you just created in step 4 to 
create a new merged dataframe.

NOTE: You will need to specify the axis and join arguments in pd.concat()"""

all_data=pd.concat([age, my_df],axis=1,join="inner")

#print(all_data)


#Exercise 2

"""Using the merged dataframe from the previous section, you will be exploring the 
relationships between different features of the data. The statsmodels package (more here) 
is an incredibly useful package for conducting statistical tests and running regressions. 
As such, it is especially appropriate for the types of questions we’re interested in here. 
For this assignment, we’ll be using the formula api from statsmodels (more here) to run some
regressions between variables in our dataset. You can load this tool into Python with 
import statsmodels.formula.api as smf."""

#Step 2.1

"""First, you’re interested in exploring if there’s a relationship between the number of 
DNMs and parental age. Use matplotlib to plot the following. All plots should be clearly 
labelled and easily interpretable.

the count of maternal de novo mutations vs. maternal age 
(upload as ex2_a.png in your submission directory)
the count of paternal de novo mutations vs. paternal age 
(upload as ex2_b.png in your submission directory)"""



y_m=list(all_data.loc[:,"maternal_dnm"])
x_m=list(all_data.loc[:,"Mother_age"])

y_p=list(all_data.loc[:,"paternal_dnm"])
x_p=list(all_data.loc[:,"Father_age"])

fig, ax2=plt.subplots()
fig, ax1=plt.subplots()

ax1.scatter(x_m,y_m)
ax2.scatter(x_p,y_p)


ax1.set_title( "Maternal de novo mutations and age" ) #set title
ax1.set_ylabel( "Maternal de novo mutations") #set x-axis label
ax1.set_xlabel("Maternal age") #sety-axis label

ax2.set_title( "Paternal de novo mutations and age" ) #set title
ax2.set_ylabel( "Paternal de novo mutations") #set x-axis label
ax2.set_xlabel("Paternal age") #sety-axis label

plt.tight_layout()
#fig.savefig( "ex2_a.png" )
#fig.savefig( "ex2_b.png" )
#plt.show()
#plt.close( fig )

#Step 2.2

"""Now that you’ve visualized these relationships, you’re curious whether they’re 
statistically significant. Perform ordinary least squares using the smf.ols() 
function to test for an association between maternal age and maternally inherited 
de novo mutations. In your README.md for this assignment, answer the following questions:

#see README.md for answers to questions"""

model1 = smf.ols(formula= "maternal_dnm ~ 1+ Mother_age", data= all_data)
results1=model1.fit()
print(results1.summary())

print(results1.pvalues["Mother_age"])

#Step 2.3

"""As before, perform ordinary least squares using the smf.ols() function, 
but this time to test for an association between paternal age and paternally 
inherited de novo mutations. In your README.md for this assignment, answer the 
following questions:

What is the “size” of this relationship? In your own words, what does this mean?
Does this match what you observed in your plots in step 6?
Is this relationship significant? How do you know?"""

model2 = smf.ols(formula= "paternal_dnm ~ 1+ Father_age", data= all_data)
results2=model2.fit()
print(results2.summary())

print(results2.pvalues["Father_age"])

#Step 2.4

"""Using your results from step 2.3, predict the number of paternal DNMs for a proband 
with a father who was 50.5 years old at the proband’s time of birth. 
Record your answer and your work (i.e. how you got to that answer) in your README.md."""

#new_observation = pd.DataFrame({"Father_age" : [50.5]})


print(results2.predict(pd.DataFrame({"Father_age" : [50.5]})))
                              
#Step 2.5

"""Next, you’re curious whether the number of paternally inherited DNMs match the 
number of maternally inherited DNMs. Using matplotlib, plot the distribution of 
maternal DNMs per proband (as a histogram). In the same panel (i.e. the same axes) 
plot the distribution of paternal DNMs per proband. Make sure to make the histograms 
semi-transparent so you can see both distributions. Upload as ex2_c.png in your submission 
directory."""

fig, ax = plt.subplots()

ax.hist(y_m, label = "female", bins = 30, alpha = 0.5)
ax.hist(y_p, label = "male", bins = 30, alpha = 0.5)
ax.legend()

ax.set_title( "De Novo Mutations" ) #set title
ax.set_xlabel("Number dnm")
ax.set_ylabel("Frequency")


plt.tight_layout()
fig.savefig( "ex2_c.png" )
plt.show()
#plt.close( fig )

#Step 2.6

"""Now that you’ve visualized this relationship, you want to test whether there is a 
significant difference between the number of maternally vs. paternally inherited DNMs 
per proband. What would be an appropriate statistical test to test this relationship? 
Choose a statistical test, and find a Python package that lets you perform this test. 
If you’re not sure where to look, the stats module from scipy (more here) provides tools 
to perform several different useful statistical tests. After performing your test, answer 
the following answers in your README.md for this assignment:

What statistical test did you choose? Why?
Was your test result statistically significant? Interpret your result as it relates 
to the number of paternally and maternally inherited DNMs."""

print(sps.ttest_ind(y_m, y_p))










