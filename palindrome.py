#!/usr/bin/python

word=input('Enter the string: ')#changed input
word_rev=str(word[::-1])

if(word == word_rev):
	print ("palindrome")#added parentheses
else:
	print ("not a palindrome")#added parentheses
