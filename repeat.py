#!/usr/bin/python

word=raw_input('Enter a string')
flag=0
for i in range(0,len(word)):
	for j in range(i+1,len(word)):
		if(word[i]==word[j]):
			print word[i]
			flag=1
			break
	if(flag==1):
		break
