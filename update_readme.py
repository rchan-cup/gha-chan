import sys

a = str(sys.argv[1])
b = str(sys.argv[2])

# with is like your try .. finally block in this case
with open('README.md', 'r') as file:
    # read a list of lines into data
    data = file.readlines()

#print data
#print "Your name: " + data[0]

# now change the 2nd line, note that you have to add a newline
data[0] = '![coverage](https://img.shields.io/badge/coverage-'+a+'%25-'+b+'])'

# and write everything back
with open('README.md', 'w') as file:
    file.writelines( data )
