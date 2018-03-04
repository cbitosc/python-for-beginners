#!/usr/bin/python

word=input('Enter a string: ')#changed input
v_count=0
word=word.lower()
for i in word:
	if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
		v_count+=1
print ("vowels:"+str(v_count)+"\nconstants:"+str(len(word)-v_count))#added parentheses
