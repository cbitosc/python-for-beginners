#!/usr/bin/python

number=int(input('Enter a number: '))
res=""
while (number!=0):
	res+=str(number%2)
	number=number//2
print (''.join(reversed(res))) #added parentheses
	
