import math, random
from brain_games.cli import message_loser


def numbers_gcd():
    num1 = random.randint(1,50)
    num2 = random.randint(1,50)
    
    numbers = [num1, num2]
    result = math.gcd(*numbers)
    
    print(f"\nQuestion {num1} {num2}")
    
    return result

def search_gcd(name):
    count = 0
    print("\nFind the greatest common divisor of given numbers.")
    
    for i in range(3):
        answer = numbers_gcd()
        user_answer = int(input("Your answer: "))
        
        if answer != user_answer:
            message = message_loser(name, answer, user_answer)
            print(message)
            break
        
        print("\nCorrect!")
        count += 1
        
    if count == 3:
        print(f"Congratulations, {name}")