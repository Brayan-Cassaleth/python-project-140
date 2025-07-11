import prompt


def welcome_user():
	print("\nWelcome to the Brain Games!")
	name_user = prompt.string("May I have your name? ")
	print(f"Hello, {name_user}!")
	return name_user


def message_loser(name, user_answer, answer):
	message = f"\n'{user_answer}' is wrong answer ;(. Correct answer was '{answer}'.\nLet's try again, {name}"
	return message
    