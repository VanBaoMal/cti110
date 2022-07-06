# This program offers an addition and subtraction quiz by generating two random numbers.
# June 29, 2022
# CTI-110 P5HW2 - Math Quiz
# Vanessa Bao-Maldonado
#

import random

# Function: to add numbers
def add_num():
    # Generate 2 random number
    anum_1 = random.randint(1,999)
    anum_2 = random.randint(1,999)

    # Add 2 numbers
    num_sum = anum_1 + anum_2
    
    # Display 2 numbers
    print(' ', anum_1)
    print('+', anum_2)
    
    # ask for user input
    print('Enter answer:', end = ' ')
    user_answer = int(input())
    
        
    tot_guesses = 0   
    while user_answer != num_sum:
        tot_guesses += 1
        # If too high
        if user_answer > num_sum:
            too_high()
            # ask for user input
            print('Try again:', end = ' ')
            user_answer = int(input())
        # If too low
        else:
            too_low()
            # ask for user input
            print('Try again:', end = ' ')
            user_answer = int(input())

    # If user answer correct
    if user_answer == num_sum:
        congrats()

    # Print number of guesses
    print('\nNumber of guesses:', tot_guesses)
    
# Function: to subtract numbers.
def sub_num():
    # Generate 2 random number
    anum_1 = random.randint(1,999)
    anum_2 = random.randint(1,999)

    # Add 2 numbers
    num_sum = anum_1 - anum_2
    
    # Display 2 numbers
    print(' ', anum_1)
    print('-', anum_2)
    
    # ask for user input
    print('Enter answer:', end = ' ')
    user_answer = int(input())

    tot_guesses = 0   
    while user_answer != num_sum:
        tot_guesses += 1
        # If too high
        if user_answer > num_sum:
            too_high()
            # ask for user input
            print('Try again:', end = ' ')
            user_answer = int(input())
        # If too low
        else:
            too_low()
            # ask for user input
            print('Try again:', end = ' ')
            user_answer = int(input())
            
    # If user answer correct
    if user_answer == num_sum:
        congrats()

    # Print number of guesses
    print('\nNumber of guesses:', tot_guesses)


# Function: Main Menu - Displays 3 options.
def main_menu():
    print('\nMAIN MENU')
    print('--------------------------------')
    print('1. Adding Random Numbers')
    print('2. Subtracting Random Numbers')
    print('3. Exit')
    print('\nPlease choose one of the menu options:', end = ' ')

# Function: print congratulations.
def congrats():
    print('Congratulations your answer is correct!')

# Function: Too low
def too_low():
    print('Sorry, guess is too low.\n')
    
# Function: Too high
def too_high():
    print('Sorry, guess is too high.\n')

    
    

# Declare variable and set to 0.   
selected_number = 0

while selected_number != 3:
    
    # Initiates call to function main menu.
    main_menu()
    # Get user user input.
    selected_number = int(input())

    # If user enters 1, call addition function.
    if selected_number == 1:
        # Call addition function
        add_num()
        
    # If user enters 2, call subtraction function.
    elif selected_number == 2:
        # Call subtraction function
        sub_num()
        
    # If the user enters 3, the program terminates.
    elif selected_number == 3:
        print('Thank you for playing. Bye!')
        
    # If user enters anything other than 1, 2, or 3 an error message is displayed.
    else:
        print('Error: Please enter 1, 2, or 3 only!')
