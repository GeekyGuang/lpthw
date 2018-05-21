# what type does input get?

a = input("a>>> ")
print(int(a) + 1) # a is str
print(a + 'apple')

b = int(input("b>>> "))
print(b + 2)

# only numbers can be converted from str to int