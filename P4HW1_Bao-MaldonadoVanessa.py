# CTI-110
# P4HW1 - Score List
# Vanessa Bao-Maldonado 
# June 25, 2022
#

# Get number of scores from user.
num_scores = int(input('How many scores do you want to enter? '))

# Define variables and list
value = 1
score_list = []

# User enters numbers (loop)
while num_scores > 0:
    #Ask user for score
    print('Enter score #', value, ':', end = ' ')
    score_input = float(input())
    
    # Evaluate if the score is valid (0-100)
    if score_input < 0 or score_input > 100:
        # If not valid notify user to enter valid score
        print('INVALID score entered!!!!')
        print('Score should be between 0 and 100')
    else:
        # If score is valid add to a list - list informative name
        score_list.append(score_input)
        # Decrease number of scores by 1
        num_scores -= 1
        # value increased by 1 for input statement
        value += 1
    
        

# Display results
print('\n--------------Results--------------')

# Display the lowest number in the list.
print('Lowest Score: ', min(score_list))

# Drop lowest score
score_list.remove(min(score_list))

# Display modified list
print('Modified list: ', score_list)

# Display the average of the numbers in the list.
number_input = len(score_list)
list_avg = sum(score_list) / number_input
print('Scores Average: ', list_avg)

# Display average as letter grade
# system uses 10-point grading scale
A_score = 90
B_score = 80
C_score = 70
D_score = 60
F_score = 0
    
# if statement to display scores, valid scores are 0 to 100
if list_avg > 100:
    print('Invalid score!')
elif list_avg >= A_score:
    print('Your grade is an A')
elif list_avg >= B_score:
    print('Your grade is a B')
elif list_avg >= C_score:
    print('Your grade is a C')
elif list_avg >= D_score:
    print('Your grade is a D')
else:
    print('Your grade is an F')

