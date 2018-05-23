# number game
print("Now, let's play a number game.")

number = float(input("Plear enter a number: "))

def random(egg):
    return egg * 23 / 2323 - 232 + 323 / 23232 * 23223

# if 0 < number <= 1:
if number in range(0, 1):
    print(f"ln{number} < 0")
elif number >= 1:
    print(f"ln{number} > 0")
elif number in range(-1, 0):
    print("What's your favorite sport？")
    print("1. football")
    print("2. pingpong")

    sport = int(input(">>> "))

    if sport == 1:
        print("What's your favorite team?")
        print("1. Real Mardrid")
        print("2. Manchester United")

        team = int(input(">>> "))
        if team == 1:
            print("Hala Mardrid!")
        elif team == 2:
            print("Glory Glory Manchester United!")
        else:
            print("Do you mind if I play football?")
    elif sport == 2:
        print("China is the best!!!\n" * 3)
    else:
        print("Enjoy yourself!")
else:
    print("Here is a random luck:", random(number))


