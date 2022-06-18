# This program takes charge, tip percentage, and tax percentage and calculates tip, tax, and total cost.
# June 18, 2022
# CTI-110 P3HW2 - Meal Tip Tax Calculator
# Vanessa Bao-Maldonado
#

def main():
    # Tax percentage
    tax_percent = 6

    # Ask user to enter the charge for food
    food_cost = float(input('Enter Food Cost: '))

    # Ask user to enter the tip for server
    tip_percent = float(input('Enter a tip amount of 15, 18, 0r 20%: '))

    # Determine if tip amount is valid
    if tip_percent == 15 or tip_percent == 18 or tip_percent == 20:
        # Calculate tip, tax, total
        calculated_tip = (tip_percent / 100) * food_cost
        calculated_tax = (tax_percent / 100) * food_cost
        calculated_total = calculated_tip + calculated_tax + food_cost
        # Display Calculated tip, Calculated tax, total cost of meal
        print('Meal price: ', food_cost)
        print('Calculated Tip: ', calculated_tip)
        print('Calculated Tax: ', calculated_tax)
        print('Total cost including tip and tax: ', calculated_total)
    else:
        print('Error: Invalid tip percentage')

# Program start
main()











