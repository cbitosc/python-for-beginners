#!/usr/bin/python

n=int(input('Enter a number: ')) #converting string to integer
first,second,temp=0,1,0
for i in range(2,n+1):
	temp=first+second
	first=second
	second=temp
	i+=1
print ("The #",n,"term in the series is: ",temp) #added parentheses and some text

