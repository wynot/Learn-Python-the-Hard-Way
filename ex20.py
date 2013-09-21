from sys import argv # Importing the module argv so that we can take inputs from the terminal line

script, input_file = argv # Assigning the inputs to variables

def print_all(f): # Defining a function 'print_all()'
	print f.read() # Giving the function an action. In this case, reading a file

def rewind(f): # Defining a new function 'rewind()'
	f.seek(0) # The action of the function seeks line 0 of a file

def print_a_line(line_count, f): # Defining a third function 'print_a_line'
	print line_count, f.readline() # The function prints the line number, then reads a line input

current_file = open(input_file) # current_file now opens the file that was input in terminal

print "First let's print the whole file:\n"

print_all(current_file) # running first function

print "Now let's rewind, kind of like a tape."

rewind(current_file) # running second function on the input file

print "Let's print three lines:"

current_line = 1 # defining the current line
print_a_line(current_line, current_file) # running the third function, defining the current_line as "1"

rewind(current_file)

print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)