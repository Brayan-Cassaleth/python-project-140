from brain_games.calculate import game_calculate
from brain_games.cli import welcome_user


name = welcome_user()


def main():
    game_calculate(name)
    

if __name__ == "__main__":
    main()