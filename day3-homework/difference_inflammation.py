"""4.) Write a function that takes two patient IDs (strings) 
as input and returns a list of the difference between their 
inflammation levels on each of the 40 days (floats). 
Embed this function in a script called difference_inflammation.py 
that defines the patient IDs as variables, executes the function, 
and prints the output."""

f= open("inflammation-01.csv", "r")

lines=f.readlines()

list=[]

for line in lines:
	line=line.rstrip()
	line_list=line.split(',')
	line_int=[]
	for value in line_list:
		col_int=float(value)
		line_int.append(col_int)
	list.append((line_int))

#print(list)

def diff_inflam(my_list,list_row1,list_row2):
	#assert type(my_list)==list, "input must be list"
	#assert type(list_row1)==int, "input must be integer"
	#assert type(list_row2)==int, "input must be integer"
	#assert len(my_list[list_row1])==len(my_list[list_row2])
	length= len(my_list[list_row1])
	difference=[]
	for i in range(length):
		pat1=my_list[list_row1][i]
		pat2=my_list[list_row2][i]
		diff=pat1-pat2
		difference.append(diff)
	return difference

#enter 2 random patient IDs to use
patient_id_1= 3
patient_id_2= 5

result=diff_inflam(list, patient_id_1, patient_id_2)
print(result)






