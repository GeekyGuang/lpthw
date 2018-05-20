print("How old are you?", end=' ') # tell print not to end the line with a newline character
age = int(input())
print(">>>> age=", repr(age))
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you are {age} old, {height} tall and {weight} heavy.")
print("So, you are {} old, {} tall and {} heavy.".format(age, height, weight))