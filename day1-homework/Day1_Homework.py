#Exercise 1: Reading in Data
#Print the number of flare-ups that the fifth patient had on the first, tenth, and last day.

print("Exercise 1")

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
print("Fifth Patient")
print("First Day")
print(list[4][0])
print("Tenth Day")
print(list[4][9])
print("Last Day")
print(list[4][-1])

#prints successfully
	
#Exercise 2: Calculating Average
#For each patient, calculate the average number of flare-ups per day. 
#Print the average values for the first 10 patients.
#These are the row averages - 
#for example, patient 1 has 5.45 flare-ups per day on average; 
#patient 2 has 5.425 flare-ups per day on average.

import numpy

print("Exercise 2")

averages=[]
for numbers in list:
	average=numpy.mean(numbers)
	averages.append(average)
print ("List of first 10 averages")
print (averages[0:10])

#Exercise 3: Finding Maximum and Minimum Values
#Using the average flare-ups per day calculated in part 2, 
#print the highest and lowest average number of flare-ups per day.

print("Exercise 3")

print("Max")
print(numpy.max(averages))
print("Min")
print(numpy.min(averages))

#Exercise 4: Differences Between Patients
#For each day, print the difference in number of flare-ups between patients 1 and 5.

print("Exercise 4")

p1=list[0]
#print(p1)
p5=list[4]
#print(p5)

difference=[]
index=0 #indicates position in list
for day1 in p1:
	for day5 in p5:
		diff=p1[index]-p5[index]
	difference.append(diff)
	index=index+1
print("List of Differences between Patient 1 and 5")
print(difference)

f.close()

"""Here are the results from the terminal
Exercise 1
Fifth Patient
First Day
0
Tenth Day
4
Last Day
1
Exercise 2
List of first 10 averages
[5.45, 5.425, 6.1, 5.9, 5.55, 6.225, 5.975, 6.65, 6.625, 6.525]
Exercise 3
Max
7.225
Min
5.225
Exercise 4
List of Differences between Patient 1 and 5
[0, -1, 0, 0, -2, 1, 1, 2, 6, -1, -1, -4, 4, 0, 4, -6, -1, -3, 6, 1, -3, -1, 2, 4, -6, -2, -8, 0, 1, 1, -5, -2, 2, 5, 1, 0, 0, 3, -1, -1]"""
