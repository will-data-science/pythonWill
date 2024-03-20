from sys import argv

script, userName = argv
prompt = "> "

print(f"Hi {userName}, I'm the {script} script.")
print(f"I'd like to ask you a few questions.")
print(f"Do you like me, {userName}?")
likes = input(prompt)

print(f"Where do you live {userName}?")
lives = input(prompt)

print(f"What kind of computer do you have {userName}?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
