from brain_games.cli import welcome_user
from brain_games.progression import game_progression


name = welcome_user()

def main():
    game_progression(name)
    
if __name__ == "__main__":
    main()