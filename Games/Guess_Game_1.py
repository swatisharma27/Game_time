'''
Guessing Game - Type 3
'''

import random
import time

def guess():
    min = 0
    max = 100
    time.sleep(2)
    guess = int(input("Take a guess between %d and %d: " % (min, max)))
    return guess

def random_num():
    number = random.randint(0, 100)
    # print(number)
    return number

def game():
    glist = []
    number = random_num()
    min = 0
    max = 100
    count = 6
    guess1 = guess()
    glist.append(guess1)
    if guess1 > 100:
        print("Incorrect Value! Try once again!")
        game()
    count -= 1

    while (guess1 in range(0, 101)) and (count != 0):
        if number == guess1:
            print("\n\tYou won! Right Guess!")
            print("The number is %d and you took %d chances to guess. " % (number, (6-count)))
            break
        elif number < guess1:
            time.sleep(1)
            print("It is too high!")
            print("You have %d chances left." % count)
            time.sleep(1)
            max = guess1
            guess2 = int(input("\nNow, take guess between %d and %d: " % (min, guess1)))
            if guess2 not in glist:
                if 0<= guess2 <= 100:
                    guess1 = guess2
                    count -= 1
                    glist.append(guess2)
                    continue
                else:
                    print("Incorrect Value! Try once again!")
                    print("You still have %d chances left." %(count))
                    continue
            else:
                print("Already used this guess! Try Another!\n")
                continue

        elif number > guess1:
            time.sleep(1)
            print("It is too low!")
            print("You have %d chances left." % count)
            time.sleep(1)
            min = guess1
            guess2 = int(input("\nNow, take guess between %d and %d: " % (guess1, max)))
            if guess2 not in glist:
                if 0 <= guess2 <= 100:
                    guess1 = guess2
                    count -= 1
                    glist.append(guess2)
                    continue
                else:
                    print("Incorrect Value! Try once again!")
                    print("You still have %d chances left." %(count))
                    continue
            else:
                print("Already used this guess! Try Another!\n")
                continue
        else:
            print("Wrong Entry! Try Again!")


    if guess1 != number:
        print("\n\tYou lost! Better luck, next time!")
        time.sleep(1)
        print("\t\tThe right guess was %d." % number)
        ask()

    elif guess1 == number and count == 0:
        print("\n\tYou won! Right Guess!")
        time.sleep(1)
        print("The number is %d and you took all %d chances to guess. " % (number, (6 - count)))
        ask()

    ask()

def ask():
    st1 = input("\nDo you want to play again? (y/n): ").lower()
    if st1 == 'y':
        print('\n\t\t\t\tWELCOME BACK!')
        print(
            '''
    Game to guess a number between 0 and 100.
The user gets 6 chances to guess the right number.
            '''
        )
        return game()
    elif st1 == 'n':
        print("\nThank you for playing! See you again!")
        raise SystemExit(0)
    else:
        print("Wrong Entry! Try this!")
        return ask()



if __name__ == '__main__':
    print("                WELCOME TO THE GUESSING GAME!       ")
    print(
        '''
            Game to guess a number between 0 and 100.
        The user gets 6 chances to guess the right number.
        '''
    )
    game()
