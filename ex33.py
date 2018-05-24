a = 0
numbers = []
top = 10
j = 2

def loop(i, top, j):
    # while i < top:
    for i in range(a, top):
        print(f"At the top i is {i}")
        numbers.append(i)

        # i += j
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

loop(a, top, j)

print("The numbers: ")

for num in numbers:
    print(num, end=" ")