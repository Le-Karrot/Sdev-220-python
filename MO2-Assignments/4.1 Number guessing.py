'''
Author: Kevin Ramirez
Date: 1/20/2026
Program: Number Guessing.py
Purpose: Ask user to guess a number from 1 to 10 till correct
'''

secret: int = 8

while True:

    guess = int(input('Guess a number from 1 to 10: '))

    if guess < secret:
        print('too low')
    elif guess > secret:
        print('too high')
    else:
        print('just right')
        break