#!/bin/env python

"""
Given the string s, produce a list composed of all the single characters from the original string
eg:
    s = "Hello"
    becomes
    l = {"H", "e", "l", "l", "o"}
"""
s = "Hi there, my name is Slim"

length = len(s)
elements = []
i = 0

while i < length:
	elements.append(s[i])
	i += 1

print elements
