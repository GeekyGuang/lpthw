# write a funtion and run it 10 different ways
from sys import argv
script, one, two = argv

def ten_ways(num, one, two, three):
    print("*" * 5, f"Way {num}", "*" * 5)
    print(f"1st is {one}")
    print("2nd is {}".format(two))
    print(f"3rd is {three}\n")

# way 1: import
i = 1
ten_ways(i, script, one, two)

# way 2: numbers
i = 2
ten_ways(i, 1, 2, 3)

# way3: variables 1
i = 3
a = "apple"
b = "orange"
c = "banana"
ten_ways(i, a, b, c)

# way4: strings
i = 4
ten_ways(i, "dog", "cat", "snake")

# way5: variables 2
i = 5
a = 23
b = 12
c = 35
ten_ways(i, a, b, c)

# way 6: variables 3
i = 6
a = input("1: ")
b = input("2: ")
c = input("3: ")
ten_ways(i, a, b, c)

# way 7: inputs
i = 7
ten_ways(i, input("1: "), input("2: "), input("3: "))

# way 8: math
i = 8
ten_ways(i, 1 + 2, 3 + 5, 23 + 53)

# way 9: variables + math 1
i = 9
a = 1
b = 2
c = 3
ten_ways(i, a + 2, b + 3, c + 5)

# way 10: variables + math 2
i = 10
a = 'apple'
b = 'orange'
c = 'banana'
ten_ways(i, a + 'skdk', b + 'djks', c + 'dsksk')

# way 11: len() + numbers
i = 11
ten_ways(i, len('apple') + 1, len('orange') + 2, len("banana") + 3)

# way 12: int(input()) + numbers
i = 12
a = int(input('> '))
b = int(input('> '))
c = int(input('> '))
ten_ways(i, a + 1, b + 2, c + 3)

