#1.) Without using any external libraries (such as numpy) 
#write a function that takes a list (of any length) of integers 
#as input and returns the mean (i.e., average). 
#Write a script called mean.py where you create the list of 
#integers, compute the mean using your function, and print it.

#!/usr/bin/env python

integer_list=[1,2,3,4,5,6]

def list_mean(my_list):
	assert type(my_list)==list, "input must be list"
	length=len(my_list)
	sum_list=sum(my_list)
	mean_list=sum_list/length
	return mean_list

result=list_mean(integer_list)
print(result)
