import random
from brain_games.calculate import message_loser

def list_numbers():
    #Numero con el que inicia la lista
    index = random.randint(1,50)
    
    #Es el multiplo con el que van aumentando
    multiplo = random.randint(1, 5)
    
    #Es el indice del numero que estara escondido
    number_random = random.randint(0, 9)
    
    numeros = ""
    count = 0
    numbers = []
    
    while count < 10:
        numbers.append(str(index))
        index += multiplo
        count += 1
    
    hidden_number = numbers[number_random]
    numbers[number_random] = ".."
    numeros = " ".join(numbers)
    print(f"\nQuestion: {numeros}")
    
    return hidden_number


def game_progression(name):
    count = 0
    print("\nWhat number is missing in the progression?")
    
    for i in range(3):
        answer = list_numbers()
        user_answer = input("Your answer: ")
        
        if answer != user_answer:
            print(message_loser(name, answer, user_answer))
            break
        
        print("Correct!")
        count += 1
    
    if count == 3:
        print(f"\nCongratulations, {name}")
            