# simple random number guessing game using 'random'
import random

def easy_mode():
    correct_num_e = random.randint(1,10)
    attempts = 0
    guess = None

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 10.")
    print("Type 'exit' to quit the game at any time.\n")

    while guess != correct_num_e:
        user_input = input(f"Enter your guess: ")

        if user_input.lower() == 'exit':
            print("You have chosen to exit. Goodbye")
            break

        if user_input.isdigit():
            guess = int(user_input)
            attempts += 1

            if guess < correct_num_e:
                print(f"Too low, try again.\n")
            elif guess > correct_num_e:
                print(f"Too high, try again.\n")
            else:
                print(f"Congratulations you guessed it!! It took you {attempts} tries")

        else:
            print(f"Invalid format please try again or type 'exit' to quit")

def medium_mode():
    correct_num_m = random.randint( 1,50)
    attempts = 0
    guess = None

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 50.")
    print("Type 'exit' to quit the game at any time.\n")

    while guess != correct_num_m:
        user_input = input(f"Enter your guess: ")

        if user_input.lower() == 'exit':
            print("You have chosen to exit. Goodbye")
            break

        if user_input.isdigit():
            guess = int(user_input)
            attempts += 1

            if guess < correct_num_m:
                print(f"Too low, try again.\n")
            elif guess > correct_num_m:
                print(f"Too high, try again.\n")
            else:
                print(f"Congratulations you guessed it!! It took you {attempts} tries")

        else:
            print(f"Invalid format please try again or type 'exit' to quit")

def hard_mode():
    correct_num_h = random.randint(1,100)
    attempts = 0
    guess = None

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Type 'exit' to quit the game at any time.\n")

    while guess != correct_num_h:
        user_input = input(f"Enter your guess: ")

        if user_input.lower() == 'exit':
            print("You have chosen to exit. Goodbye")
            break

        if user_input.isdigit():
            guess = int(user_input)
            attempts += 1

            if guess < correct_num_h:
                print(f"Too low, try again.\n")
            elif guess > correct_num_h:
                print(f"Too high, try again.\n")
            else:
                print(f"Congratulations you guessed it!! It took you {attempts} tries")

        else:
            print(f"Invalid format please try again or type 'exit' to quit")

while True:
    print(f"1) Easy")
    print(f"2) Medium")
    print(f"3) Hard")
    diff = int(input(f"Choose difficulty: "))

    if diff == 1:
        easy_mode()

    elif diff == 2:
        medium_mode()

    elif diff == 3:
        hard_mode()

    else:
        print(f"Invalid Input")

    play_again = input("Play again? (y/n): ")

    if play_again.lower() != 'y':
        print("Thanks for playing!")
        break
