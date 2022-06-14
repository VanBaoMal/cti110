# This program takes charge, tip percentage, and tax percentage and calculates tip, tax, and total cost.
# June 14, 2022
# CTI-110 P2HW1 - Meal Tip Tax Calculator
# Vanessa Bao-Maldonado
#

# Ask user to enter the charge for food
food_cost = float(input('Enter Food Cost:'))

# Ask user to enter theTip for server
tip_percent = float(input('Enter Tip Percentage:'))

# Ask user to enter the Tax amount
tax_percent = float(input('Enter Tax Percentage:'))

# Calculate tip, tax, total
calculated_tip = (tip_percent / 100) * food_cost
calculated_tax = (tax_percent / 100) * food_cost
calculated_total = calculated_tip + calculated_tax + food_cost

# Display Calculated tip, Calculated tax, total cost of meal
print('Calculated Tip:', calculated_tip)
print('Calculated Tax:', calculated_tax)
print('Total cost including tip and tax:', calculated_total)


