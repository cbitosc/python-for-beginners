#!/usr/bin/python

x=int(input('Enter a number: '))#converting input to integer
count=0
for i in range(1,x+1):
	if(x%i==0):
		count+=1
print ("no of divisors:"+str(count))#added parentheses
