#!/usr/bin/python

a=int(input('Enter the starting number of the range: '))#converting string to integer
b=int(input('Enter the last number of the range: '))#converting string to integer
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
print ("# of prime numbers in range:",count) #added parentheses and text

	
