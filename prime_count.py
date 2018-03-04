#!/usr/bin/python

a=input('Enter the starting number of the range')
b=input('Enter the last number of the range')
count=0
for i in range(a,b+1):
	flag=0
	for j in range(2,i):
		if(i%j==0):
			flag=1
		if(flag==1):
			break
	if(flag==0):
		count+=1
print count

	
