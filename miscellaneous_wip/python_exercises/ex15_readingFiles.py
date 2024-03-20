from sys import argv

script, filename = argv

text = open(filename)

print(f"Here's your file {filename}:")
print(text.read())

print("Type the filename again:)")
fileAgain = input("> ")

textAgain = open(fileAgain)

print(textAgain.read())
