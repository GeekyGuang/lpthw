from sys import argv
script, one, two = argv
# This one is like your scripts with argv
def print_two(*cat): # how about changing args to cat?
    arg1, arg2 = cat
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just take one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments
def print_none():
    print("I got nothin'.")

print_two(one, two)
print_two_again(one, two)
print_one("First!")
print_none()