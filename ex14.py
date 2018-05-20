from sys import argv

script, user_name, friend = argv
prompt = f'{script}>>> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you some questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
live = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt + '$')

print(f"How do you think of {friend}?")
think = input(prompt)

print(f"""Alright, so you said {likes} about liking me.
You live in {live}. Not sure where that is.
You have got a {computer} computer.
And you think {friend} is {think}.
 Nice.""")