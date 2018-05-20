# Use argv to get a filename
from sys import argv

script, filename = argv
# Open the file
txt = open(filename) # What you get back from open is a file object
# txt.close()
# print out the contents of the file
print(f"Here's your file {filename}:")
print(txt.read())


# Use input to get a filename
print("Type the filename again:")
file_again = input('> ')

txt_again = open(file_again)
print(txt_again.read())



