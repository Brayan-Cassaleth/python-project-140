import random
from brain_games.cli import message_loser


def operacion():
    operator = "+-*"
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    item = random.randint(0, len(operator) - 1)
    
    print(f"\nQuestion: {num1} {operator[item]} {num2}")
    
    if operator[item] == "+":
        result = num1 + num2
    
    if operator[item] == "-":
        result = num1 - num2
    
    if operator[item] == "*":
        result = num1 * num2
        
    return result


def game_calculate(name):
    count = 0
    print("\nWhat is the result of the expression?")
    
    for i in range(3):
        answer = operacion()
        user_answer = int(input("Your answer: "))

        if answer != user_answer:
            message = message_loser(name, user_answer, answer)
            print(message)
            break

        print("Correct!")
        count += 1

    if count == 3:
        print(f"\nCongratulations, {name}")