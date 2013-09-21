def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b


#print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide (100, 2)

#print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for extra credit, type it in anyway
#print "Here is a puzzle."

#what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

#print "That becomes: ", what, "Can you do it by hand?"

print "Here's me trying my own"

def divultiply(a, b, c, d):
	print "Let's divultiply this bitch"
	return a + (b - (c * (d / 2)))

misc = divultiply(age, height, weight, iq)

print misc

print "boom shakalaka"

print "Attempt #2"

def multivide(a,b,c):
	print "Let's multivide this punk, aka %d, %d, and the infamous %d" % (a, b, c)
	return a * (b - (c / 100))

misc2 = multivide(age, height, weight)

print misc2

who = multiply(age, subtract(height, divide(weight, 100)))

print who