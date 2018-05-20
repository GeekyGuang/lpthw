from sys import argv

script, first, second, third = argv  # unpack arguments to 4 variables
# how to only unpack the forth argument?

print(">>>> argv= ", repr(argv))

print(f"The script is called: {script}")
print("Your first variable is: {}".format(first))
print("Your second variable is:", second)
print("Your thrid variable is:", third)

favor = input("Which one do you like the most? ")
print("So, You like \"{}\" the most.".format(favor))

