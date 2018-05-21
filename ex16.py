from sys import argv

script, filename = argv

print(f"In We are going to earse {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

# if open() with 'w' mode, truncate() is not necessary
# print("Truncating the file. Goodbye!")
# target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# target.write(line1)
# target.write('\n')
# target.write(line2)
# target.write('\n')
# target.write(line3)
# target.write('\n')
target.write(line1+'\n'+line2+'\n'+line3+'\n')

print("And finally, we close it.")
target.close() # this is necessary

target = open(filename)
print(target.read()) # You can only read after closing the file
target.close()

