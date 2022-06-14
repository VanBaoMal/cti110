# CTI-110
# P2HW2 - List and Sets
# Vanessa Bao-Maldonado 
# June 14, 2022
#

# Ask the user to enter 6 numbers.
num_1 = float(input('Enter your 1st number: '))
num_2 = float(input('Enter your 2nd number: '))
num_3 = float(input('Enter your 3rd number: '))
num_4 = float(input('Enter your 4th number: '))
num_5 = float(input('Enter your 5th number: '))
num_6 = float(input('Enter your 6th number: '))

# Store the numbers in a list and display list.
user_list = [num_1, num_2, num_3, num_4, num_5, num_6]
print('\nCreated list: ', user_list)

# Display the lowest number in the list.
print('Smallest number in the list: ', min(user_list))

# Display the highest number in the list.
print('Largest number in the list: ', max(user_list))

# Display the total of the numbers in the list.
print('Sum of all the number in the list: ', sum(user_list))

# Display the average of the numbers in the list.
number_input = len(user_list)
list_avg = sum(user_list) / number_input
print('The average of the numbers in the list: ', list_avg)

#Convert to list to a set and display set.
created_set = set(user_list)
print('\nCreated set:', created_set)
