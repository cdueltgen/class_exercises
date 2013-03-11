#!/bin/env python

"""
Given the string s, excise characters 6 through 12, inclusive
eg:
    s = "Hello, good sir"
    becomes 
    s = "Hello sir"
"""
s = "Hi there, my name is Slim"

s1 = s[0:6] + s[13:]
print s1