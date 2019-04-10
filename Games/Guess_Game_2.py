'''
Guessing Game - Type 1
'''

import random
import time

def guess():
    min = 0
    max = 100
    print("Now, Program will guess the number.")
    time.sleep(1)
    print("Okay Program, start guessing:")
    time.sleep(1)
    guess = random.randint(0, 100)
    print(guess)
    return guess

def random_num():
    time.sleep(1)
    number = int(input("Enter the number in your head:"))
    if 0 <= number <= 100:
        return number
    else:
        time.sleep(1)
        print("\nWrong Entry. Please try again.")
        print("Range of number selection is between 0 and 100.")
        print("\n")
        return random_num()

def game():
    number = random_num()
    min = 0
    max = 100
    time.sleep(2)
    guess1 = guess()
    count = 0
    glist = []

    while (guess1 in range(0, 101)):
        if number == guess1:
            print("Program ran well! Right Guess!")
            print("The number is %d and it took %d chances. " % (number, count))
            break

        elif number < guess1:
            print("It is too high!")
            time.sleep(2)
            max = guess1
            print("\nProgram, take guess between %d and %d:" % (min, guess1))
            time.sleep(2)
            guess2 = random.randint(min, guess1)
            print(guess2)
            if guess2 not in glist:
                if 0 <= guess2 <= 100:
                    guess1 = guess2
                    count += 1
                    glist.append(guess2)
                    continue
                else:
                    print("Incorrect Value! Try once again!")
                    continue
            else:
                print("Already used this guess! Try Another!\n")
                continue

        elif number > guess1:
            print("It is too low!")
            time.sleep(2)
            min = guess1
            print("\nProgram, take guess between %d and %d:" % (guess1, max))
            time.sleep(2)
            guess2 = random.randint(guess1, max)
            print(guess2)
            if guess2 not in glist:
                if 0 <= guess2 <= 100:
                    guess1 = guess2
                    count += 1
                    glist.append(guess2)
                    continue
                else:
                    print("Incorrect Value! Try once again!")
                    continue
            else:
                print("Already used this guess! Try Another!\n")
                continue

        else:
            print("Wrong Entry! Try Again!")
    ask()

def ask():
    st1 = input("\nDo you want to play again? (y/n): ").lower()
    if st1 == 'y':
        time.sleep(2)
        print('\n\t\t\t\t\tWELCOME BACK!')
        print('''
            \t What is the game?
        ....................................
        A number will be entered by the user.
        And the program will guess the number.
                        ''')
        return game()
    elif st1 == 'n':
        print("\nThank you for playing! See you again'!")
        raise SystemExit(0)
    else:
        print("Wrong Entry! Try this!")
        return ask()

if __name__ == '__main__':
    print("\n\t\t\tWELCOME TO THE GUESSING GAME!")
    print('''
        \t\tWhat is the game?
        ....................................
        A number will be entered by the user.
        And the program will guess the number.
                ''')
    game()
