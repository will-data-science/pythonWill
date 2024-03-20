formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))

# This would throw an error
# print(formatter.format(1))

print(formatter.format("a", "b", "c", "d"))

# Can use a mix of data types
print(formatter.format("a", 1, "b", 2))

print(formatter.format(True, True, False, False))

print(formatter.format("try to", "create a", "full", "sentence!"))

days = "Mon Tue Wed Thu Fri Sat Sun"
# Similar to scala, etc. \n will insert new paragraphs
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug\nSep\nOct\nNov\nDec"

print("these are the days: ", days)
print("these are the months: ", months)

# Use triple quotes to insert paragraphs yourself
print("""
There's something going on here.
We are adding new lines
Yay!
""")
