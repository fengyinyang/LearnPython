from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print script
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

def new_fun():
	return "new fun"

print "Type the filename again:"