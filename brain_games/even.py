import random
from brain_games.cli import message_loser


def game_even(name):
	cont = 0
	print('\nAnswer "yes" if the number is even, otherwise answer "no".')

	for item in range(3):
		number = random.randint(1, 100)
		answer = "yes" if number % 2 == 0 else "no"
		print(f"\nQuestion: {number}")
		user_answer = input("Your answer: ").lower()

		if user_answer != answer:
			message = message_loser(name, user_answer, answer)
			print(message)
			break

		print("Correct!")
		cont += 1

	if cont == 3:
		print(f"\nCongratulations, {name}")
