#!/usr/bin/python

import itertools
array= list()
num = input("Enter how many elements you want:")
for i in range(1,int(num)+1):
    array.append(int(input('Enter the number')))
for i in range(0,num+1):
	print list(itertools.combinations(array,i))
