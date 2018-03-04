#!/usr/bin/python

word=input('Enter a string: ')#changed input
flag=0
for i in range(0,len(word)):
	for j in range(i+1,len(word)):
		if(word[i]==word[j]):
			print ("the first repeating letter is:",word[i])#added parentheses
			flag=1
			break
	if(flag==1):
		break
