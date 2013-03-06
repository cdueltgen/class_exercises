from arithmetic import add
from arithmetic import subtract
from arithmetic import multiply
from arithmetic import divide
from arithmetic import square
from arithmetic import cube
from arithmetic import power
from arithmetic import mod

while 1:
	my_input = raw_input("> ")
	token = my_input.split(" ")
	if token[0] == 'q':
		break
	elif token[0] == 'add':
		result = add(token[1], token[2])
		print result
	elif token[0] == 'subtract':
		result = subtract(token[1], token[2])
		print result
	elif token[0] == 'multiply':
		result = multiply(token[1], token[2])
		print result
	elif token[0] == 'divide':
		result = divide(token[1], token[2])
		print result
	elif token[0] == 'square':
		result = square(token[1])
		print result
	elif token[0] == 'cube':
		result = cube(token[1])
		print result
	elif token[0] == 'power':
		result = power(token[1], token[2])
		print result
	elif token[0] == 'mod':
		result = mod(token[1], token[2])
		print result
	else:
		print "I don't know that one"
