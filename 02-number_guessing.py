# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 09:25:42 2022

@author: patry
"""

import random as rd

def intro():
    print('Welcome to the NUMBER GUESSING!')
    print('\nJust type a number to guess Python\'s number!')
    rand_number = rd.randint(1,100)
    print('Python\'s number is already generated. \nLET\'S START GUESSING!')
    guess(rand_number)

def guess(number):
    i = 0
    while True:
        i += 1
        try:
            answer = int(input('Choose your number (1-100): '))
            if answer > 0 and answer <= 100:
                if answer == number:
                    print('Success! {} is correct number!'.format(answer))
                    print('You succeed after {} guesses.'.format(i))
                    break
                elif answer > number:
                    print('Your number is too high. Try again.')
                    if i == 5:
                        hint(1, number)
                    elif i == 10:
                        hint(2, number)
                    continue
                elif answer < number:
                    print('Your number is too low. Try again.')
                    if i == 5:
                        hint(1, number)
                    elif i == 10:
                        hint(2, number)
                    continue
            else:
                1/0
        except ValueError:
            print('You need to type an integer. Try again.')
            continue
        except ZeroDivisionError:
            print('You need to choose a number from 1 to 100. Try again.')
            continue
    again()

def hint(number_of_hint, number):
    while True:
        try:
            if number_of_hint == 1:
                answer = str(input('Do you need a small hint? (y/n): '))
                if answer == 'y':
                    print('HINT! You are looking for an {} number.'
                          .format(even_odd(number)))
                    break
                elif answer == 'n':
                    break
                else:
                    1/0
            elif number_of_hint == 2:
                answer = str(input('Do you need a strong hint? (y/n): '))
                if answer == 'y':
                    print('HINT! You are looking for a number divisible by {}.'
                          .format(rd.choice(divisions(number))))
                    break
                elif answer == 'n':
                    break
                else:
                    1/0
        except ValueError and ZeroDivisionError:
            print('You need to choose: \'y\' - yes, \'n\'- no. Try again.')
            continue

def even_odd(number):
    if number % 2 == 0:
        return 'even'
    else:
        return 'odd'

def divisions(number):
    divisions = []
    for i in range(1, number):
        if number % i == 0:
            divisions.append(i)
    return divisions

def again():
    while True:
        try:
            answer = str(input('Do you want to guess again? (y/n): '))
            if answer == 'y':
                intro()
                break
            elif answer == 'n':
                input('Good bye!')
                break
            else:
                1/0
        except ValueError and ZeroDivisionError:
            print('You need to choose: \'y\' - yes, \'n\'- no. Try again.')
            continue

intro()