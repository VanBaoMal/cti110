# This program takes an expense and calculates and displays a 6% tax, monthly charge, and annual charge.
# June 8, 2022
# CTI-110 P1HW2 - Basic Math
# Vanessa Bao-Maldonado
#

# Ask user to enter the name of the expense.
bill_name = input('Enter name of expense: ')

# Ask user to enter how much they are charged for that expense/bill monthly (without tax).
charge_pretax = int(input('Enter monthly charge: '))

# Calculate monthly tax
tax = .06
month_tax = charge_pretax * tax

# Calculate amount paid monthly
month_charge = month_tax + charge_pretax

# Calculate amount paid for entire year.
annual_charge = month_charge * 12

# Display results: Bill, before tax amount, monthly tax, monthly charge, and annual charge.
print()
print('Bill:', bill_name, '---------', 'Before Tax:  $', f'{charge_pretax:.2f}')
print('Monthly Tax:      $', f'{month_tax:.2f}')
print('Monthly Charge:   $', f'{month_charge:.2f}')
print('Annual Charge:    $', f'{annual_charge:.2f}')
