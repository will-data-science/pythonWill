from sys import argv # argument variable

# In terminal you run a program like this
# python var1 var2 ... varn

# argv holds the arguments you pass to your python script when you run it
# This line unpacks it and assigns them to 4 separate variables
# The first is always the script name
# You will get an error if you don't provide enough args
script, first, second, third = argv
print("The script is called: ", script)
print("Your first variable is: ", first)
print("Your second variable is: ", second)
print("Your third variable is: ", third)
