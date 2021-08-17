typesOfPeople = 10
# f is for format
x = f"there are {typesOfPeople} types of people"

binary = "binary"
doNot = "do not"

y = f"those who know {binary} and those who {doNot}"

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

# Python recognizes False & True as booleans
hilarious = False
jokeEvaluation = "Isn't that joke so funny?! {}"

# here we use the format method to insert the variable into the brackets
print(jokeEvaluation.format(hilarious))

w = "this is the left side of ..."
e = "a string with a right side."

print(w + e)
