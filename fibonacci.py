#!/usr/bin/python

n=input('Enter a number')
first,second,temp=0,1,0
for i in range(2,n+1):
	temp=first+second
	first=second
	second=temp
	i+=1
print temp

