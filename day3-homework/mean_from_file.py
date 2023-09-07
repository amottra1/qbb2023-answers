"""2.) Use the function from part 1 to write a Python script 
called mean_from_file.py that computes and prints the mean of 
a series of integers from a data file (e.g., “my_integers.txt”) 
where the data contain a set of integers, one per line. 
[Optional: Write your code so that the user can specify the 
name of that file from the command line (hint: use sys.argv).]"""

import sys

#!/usr/bin/env python

fname=sys.argv[1] 
fs=open(fname)

integer_list=[]

for i in fs:
	integer_list.append(int(i))
	

def list_mean(my_list):
	assert type(my_list)==list, "input must be list"
	length=len(my_list)
	sum_list=sum(my_list)
	mean_list=sum_list/length
	return mean_list

result=list_mean(integer_list)
print(result)

#input to command line needs to be to run file
#then txt file to use as list