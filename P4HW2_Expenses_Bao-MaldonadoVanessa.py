# CTI-110
# P4HW2 - Expenses
# Vanessa Bao-Maldonado
# June 26, 2022


# Prompt user to enter amount in account in which money will be withdrawn from.
original_amount = float(input('Enter starting amount in account: $'))

# Define variable for expense count and while loop and list
num_expenses = 1
deduct_expenses = 'y'
expenses_list = []

while deduct_expenses == 'y' or deduct_expenses == 'Y':
    # Prompt user to enter amount of first expense.
    print('Enter expense ', num_expenses, ':', end = ' ')
    user_expense = float(input())
    expenses_list.append(user_expense)
    # Running count for number of expenses
    num_expenses += 1
    # Ask user if he/she would like to enter another expense.
    print('Do you want to enter another expense? (y/n)', end = ' ')
    deduct_expenses = str(input())

# Display amount in account BEFORE expenses subtracted
print('\nAmount in account before expenses subtracted $', original_amount)

# Display number of expenses entered
print('Number of expenses entered: ', num_expenses-1)

# Calculate sum of expenses and substract from original amount
sum_expenses = sum(expenses_list)
final_amount = original_amount - sum_expenses

# Display amount in account AFTER expenses subtracted
print('Amount in account AFTER expenses subtracted is $', final_amount)
