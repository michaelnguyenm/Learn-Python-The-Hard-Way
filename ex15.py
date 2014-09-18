# This line imports the sys module/package and allows you to use the argument variables
from sys import argv

# This line assigns variables script and filename to what was used for argv
script, filename = argv

# This lines opens the file and assigns it to txt
txt = open(filename)

# This prints a line and the filename... and then reads txt
print "Here's your file %r:" % filename
print txt.read()

# This asks to type the file name again for input and assigns it to file_again
print "Type the filename again:"
file_again = raw_input("> ")

# This line opens the file_again and then assigns it to txt_again
txt_again = open(file_again)

# This line prints what is in txt_again
print txt_again.read()