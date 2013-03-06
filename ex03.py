def inches_to_cm(inches):
	"""
	converts inches to centimeters

	Arguments:
	inches -- input in inches

	Return:
	A real number that is the value of inches in centimeters

	Examples:
	>>> inches_to_cm(1)
	2.54
	>>> inches_to_cm(10)
	25.4
	"""
	return inches * 2.54

def feet_to_inches(feet):
	"""
	converts feet to inches

	Arguments:
	feet -- input in feet

	Return:
	A real number that is the value of feet in inches

	Examples:
	>>> feet_to_inches(2)
	24
	>>> feet_to_inches(5)
	60
	"""
	return feet * 12

def yards_to_feet(yards):
	"""
	converts yards to feet

	Arguments:
	yards --- input in yards

	Return:
	A real number that is the value of yards in feet

	Examples:
	>>> yards_to_feet(5)
	15
	>>> yards_to_feet(10)
	30
	"""
	return yards * 3

def rods_to_yards(rods):
	"""
	converts rods to yards

	Arguments:
	rods -- input in yards

	Return:
	A real number that is the value of rods in yards

	Examples:
	>>> rods_to_yards(2)
	11
	>>> rods_to_yards(10)
	55
	"""
	return rods * 5.5

def furlongs_to_rods(furlongs):
	"""
	converts furlongs to rods

	Arguments:
	furlongs -- input in furlongs

	Return:
	A real number that is the value of rods in yards

	Examples:
	>>> furlongs_to_rods(5)
	200
	>>> furlongs_to_rods(10)
	400
	"""
	return furlongs * 40

def miles_to_furlongs(miles):
	"""
	converts miles to furlongs

	Arguments:
	miles -- input in miles

	Return:
	A real number that is the value of rods in yards

	Examples:
	>>> miles_to_furlongs(5)
	40
	>>> miles_to_furlongs(10)
	80
	"""
	return miles * 8

def inside_circle(r, x, y):
	"""
	returns a value of true if a point (x,y) is inside of a circle of 
	radius r that is centered around the origin

	Arguments:
	r -- the radius of the circle
	x -- the x coordinate of the point we are testing
	y -- the y coordinate of the point we are testing

	Return:
	True if the point is inside the circle, False if outside

	Examples:
	>>> inside_circle(1, .5, .5)
	True
	>>> inside_circle(1, 2, 2)
	False
	"""
	return r > math.sqrt((x * x) + (y * y))

def new_price(orig_price, weeks):
	"""
	A function that determines the sale price of an item based on its
	original price and how long it's been on the shelf

	Arguments:
	orig_price -- the original price of the item
	weeks -- how long has it been on sale

	Return:
	the adjusted price of the item

	Examples:
	>>> new_price(10, 2.5)
	7.5
	>>> new_price(10, 4)
	2.5
	"""

	if weeks < 2:
		return orig_price
	elif weeks < 3:
		return orig_price * .75
	elif weeks < 4:
		return orig_price * .5
	else:
		return orig_price * .25

def production(hour, num_workers):
	"""
	A function that takes the hour of the day and the number of workers
	and calculates how many pieces they produced in that hour

	Arguments:
	hour -- the hour of the day in 24 hour format
	num_workers -- the number of workers in that hour

	Return:
	The calculated number of items

	Examples:
	>>>production(0800, 10)
	300
	>>>production(1200, 20)
	800
	"""
	if hour >= 0600 and hour < 1000:
		return workers * 30
	elif hour >=1000 and hour < 1400:
		return workers * 40
	elif hour >=1400 and hour < 1800:
		return workers * 35
	else:
		return 0

def bill_amount()