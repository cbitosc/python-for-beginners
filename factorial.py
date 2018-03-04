#!/usr/bin/python

x=int(input('Enter a digit: '))#converting input to integer from string
fact=1
for i in range(1,x+1):
	fact*=i
print (fact) #added parentheses
