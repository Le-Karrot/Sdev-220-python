'''
Author: Kevin Ramirez
Date: 1/20/2026
Program: LAB.py
Purpose: Program will accept students name, gpa, and test if the student qualifies for Deans or Honor Roll list.
'''

#creating constants
DEANS_LIST: float = 3.5 
HONOR_ROLL: float = 3.25

#creating variables
first_name: str = ''
gpa: float = 0.0

#creating sentienl value
SENTINEL: str = 'ZZZ'

#creating while loop

while True:

    first_name = input('Enter students first name(ZZZ to quit): ')
    
    if first_name.upper != SENTINEL:

        gpa = float(input('Enter students GPA: '))

        if gpa >= DEANS_LIST:
            print(f"The student {first_name} has made the Dean's list with a {gpa}!")
            
        elif gpa <= HONOR_ROLL:
            print(f"The student {first_name} has made the Honor roll with a {gpa}!")                   
    else:
        break