oil_change = '$35'
tire_rotation = '$19'
car_wash = '$7'

service = input("Enter desired auto service:\n")
print("You entered:", service)

if service == 'Oil change' or service == 'oil change':
    print('Cost of oil change:', oil_change)
elif service == 'Tire rotation' or service == 'tire rotation':
    print('Cost of tire rotation:', tire_rotation)
elif service == 'Car wash' or service == 'Car wash':
    print('Cost of car wash:', car_wash)
else:
    print('Error: Requested service is not recognized')