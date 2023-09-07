"""Extend the Day-1 homework without using any external libraries 
(such as numpy) unless otherwise noted to analyze data from 
inflammation.csv:

3.) Write a function that takes a patient ID (string) as input 
and returns the mean inflammation level across the 40 days (float) 
for that given patient. Do not use any external libraries 
(such as numpy). Embed this function in a script called 
mean_inflammation.py that defines the patient ID as a variable, 
executes the function, and prints the output."""

#actually use a row index for patient ID
#then input a random row index and print to check code

f= open("inflammation-01.csv", "r")

lines=f.readlines()

list=[]

for line in lines:
	line=line.rstrip()
	line_list=line.split(',')
	line_int=[]
	for value in line_list:
		col_int=int(value)
		line_int.append(col_int)
	list.append((line_int))

#print(list)

def mean_inflam(my_list,list_row):
	#assert type(my_list)==list, "input must be list"
	#assert type(list_row)==int, "input must be integer"
	length=len(my_list[list_row])
	sum_list=sum(my_list[list_row])
	mean_list=sum_list/length
	return mean_list

patient_id=5

result=mean_inflam(list,patient_id)
print(result)














