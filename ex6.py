# assign 10 to types_of_people
types_of_people = 10
# assign the f-string to x (insert types_of_people in the string)
x = f"There are {types_of_people} types of people."

# assign binary to binary
binary = "binary"
# assign don't to do_not
do_not = "don't"
# assign the f-string to y (insert binary and do_not in the string)
y = f"Those who konw {binary} and those who {do_not}."
# print(">>>>> after assign y", y)

# export x
print(x)
# export y
print(y)

# export the f-string (insert x in the string)
print(f"I said {x}")
print(f"I also said '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny! {}"

# export joke_evaluation string (insert hilarious in it)
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)