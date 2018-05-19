tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
""" # end up with newline

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

print("My favorite song is \"love story\"\n")

formatter = "{} {} {} {}"

print(formatter.format('A\a', 'B\b', 'C\f', 'D\v'))
