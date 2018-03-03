#!/usr/bin/python

word1=raw_input('enter first string')
word2=raw_input('enter second string')

if(sorted(word1)==sorted(word2)):
	print "anagram"
else:
	print "not an anagram"

