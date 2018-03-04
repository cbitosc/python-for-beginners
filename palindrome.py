#!/usr/bin/python

word=raw_input('Enter the string')
word_rev=str(word[::-1])

if(word == word_rev):
	print "palindrome"
else:
	print "not a palindrome"
