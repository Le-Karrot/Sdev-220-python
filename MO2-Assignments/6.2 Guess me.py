'''
Author: Kevin Ramirez
Date: 1/20/2026
Program: Guess me.py
Purpose: write a while loop that guesses the number through increments
'''

guess_me: int = 7
number: int = 1


while True:

    if number < guess_me:
        print('too low')
    elif number == guess_me:
        print('found it!')
        break 
    elif number > guess_me:
        print('oops')
        break
    number += 1

#the prompt in the chapter 6 for 6.2 is asking to break out the loop when we find the number but that mean it'll never reach the last elif statement so it makes it useless to implement