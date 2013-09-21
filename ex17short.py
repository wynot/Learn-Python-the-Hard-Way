# we could do these two on one line too, how?
input = open('test.txt')
indata = input.read()

output = open('copied.txt', 'w')
output.write(indata)

output.close()
input.close()