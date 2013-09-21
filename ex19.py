# This defines a function 'cheese_and_crackers'. It says to print the two variables provided in the specified destinations
#def cheese_and_crackers(cheese_count, boxes_of_crackers):
#	print "You have %d cheeses!" % cheese_count
#	print "You have %d boxes of crackers!" % boxes_of_crackers
#	print "Man that's enough for a party!"
#	print "Get a blanket.\n"

# Instead of setting each of the variables within the function, we set them both on one line using the function syntax
#print "We can just give the function numbers directly:"
#cheese_and_crackers(20,30)

# We can define variables within a script
#print "OR, we can use variables from our script:"
#amount_of_cheese = 10
#amount_of_crackers = 50

#cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# This runs the function using variables set using math
#print "We can even do math inside too:"
#cheese_and_crackers(10 + 20, 5 + 6)

# This runs the function using both variables and math as inputs
#print "And we can combine the two, variables and math:"
#cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

print "This is me writing a brand spanking new function"

def func(AAA, BBB):
	print "Did you hear about %r?" % AAA
	print "Oh yeah, total bitch. Almost as much as %r" % BBB

func('Bob', 'Mike') #1
func(100, 200) #2

Cinderella = 1300
Snow_White = 234

func(Cinderella, Snow_White)
func(Cinderella + 4, Snow_White * 4) #4
func(Cinderella+Snow_White, Snow_White-Cinderella) #5

argh = Cinderella + Snow_White
argh3 = Snow_White * Cinderella
func(argh3, argh)




