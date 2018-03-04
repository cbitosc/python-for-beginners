#!/usr/bin/python

word1=input('enter first string: ') #changed to input
word2=input('enter second string: ')#changed to input

if(sorted(word1)==sorted(word2)):
	print ("anagram") #added parentheses
else:
	print ("not an anagram")#added parentheses

