# This program outputs a students letter grade.
# CTI-110
# P3HW1 - Debugging
# Vanessa Bao-Maldonado 
# June 18, 2022
#

def main():
    # This program takes a number grade and outputs a letter grade.
    score = int(input('Please enter score:\n'))
    
    # system uses 10-point grading scale
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    F_score = 0
    
    # if statement to display scores, valid scores are 0 to 100
    if score > 100:
        print('Invalid score entered!')
    elif score >= A_score:
        print('Your grade is an A')
    elif score >= B_score:
        print('Your grade is a B')
    elif score >= C_score:
        print('Your grade is a C')
    elif score >= D_score:
        print('Your grade is a D')
    elif score >= F_score:
        print('Your grade is an F')
    else:
        print('Invalid score entered!')
        








# program start
main()
