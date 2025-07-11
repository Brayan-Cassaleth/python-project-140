from brain_games.cli import welcome_user
from brain_games.even import game_even


name = welcome_user()


def main():
	game_even(name)


if __name__ == "__main__":
	main()
