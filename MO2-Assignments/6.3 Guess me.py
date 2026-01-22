'''
Author: Kevin Ramirez
Date: 1/20/2026
Program: Guess me2.py
Purpose: use a for loop to guess the number
'''

guess_me: int = 5

for number in range(10):
    if number < guess_me:
        print('too low')
    elif number == guess_me:
        print('found it!')
        break
    elif number > guess_me:
        print('oops')
        break

#same prompt here where we break out the loop when we find the number, so last elif is never checked