#!/usr/bin/python

import itertools
array= list()
num = int(input("Enter how many elements you want: "))#convert input to integer
for i in range(1,int(num)+1):
    array.append(int(input('Enter the number: ')))
for i in range(0,num+1):
	print (list(itertools.combinations(array,i)))#added parentheses
