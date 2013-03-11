#!/bin/env python

s = ""

"""
Given a multiline string 's', print each line along with the line number

eg:
    mystr = "Sorry,\nMy people need me\nI must go"

    prints

    1. Sorry,
    2. My people need me
    3. I must go.

"""
mystr = "Sorry,\nMy people need me\nI must go"

mystr_split = mystr.split("\n")
print mystr_split

line_number = 1
for line in mystr_split:
	print "%d. %s" % (line_number, line)
	line_number += 1