from random import randint
from sys import exit

name = raw_input("Howdy, what's your name? ")
print "%s, I'm thinking of a number between 1 and 100. Try to guess my number" % name

my_num = randint(1,100)
print my_num
#check_num(my_num, name)
tries = 0

while True:
	tries += 1
	guess = int(raw_input("Your guess? "))
	if guess < my_num:
		print "Your guess is too low. Try again."
	elif guess > my_num:
		print "Your guess is too high. Try again."
	else:
		print "Well done, %s! You found my number in %d tries!" % (name, tries)
		exit(0)
