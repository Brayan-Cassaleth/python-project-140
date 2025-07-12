from brain_games.cli import welcome_user
from brain_games.gcd import search_gcd


name = welcome_user()

def main():
    search_gcd(name)
    

if __name__ == "__main__":
    main()