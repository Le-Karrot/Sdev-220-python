'''
Author: Kevin Ramirez
Date: 1/20/2026
Program: True or False.py
Purpose: matching characteristics with if else statements
'''
print('Select true or false for following characteristic: ')

#creating a more interactive app 

small = int(input('Small(1 for true or 0 for false): '))
             
green = int(input('Green(1 for true or 0 for false): ') )     

if small == False and green == True:
    print('it\'s a watermelon')
elif small == False and green == False:
    print('it\'s a pumpkin')
elif small == True and green == False:
    print('it\'s a cherry')
elif small == True and green == True:
    print('it\'s a pea')
else:
    print('Invalid input')
