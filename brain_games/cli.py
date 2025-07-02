import prompt


def welcome_user():
	print("Welcome to the Brain Games!")
	name_user = prompt.script("May I have your name?")
	print(f"Hello, {name_user}!")
