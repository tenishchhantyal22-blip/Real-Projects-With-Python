## Inputs we need from user
# Total Rent
# Total food ordered
# Electricity
# Charge per unit
# Number of person

## output
# total amount you've to pay

rent = int(input("Enter your rent = "))
food = int(input("Enter the amount of food ordered = "))
electricity = int(input("Enter the total of electricity spend = "))
charge_per_unit = int(input("Enter the charge per unit = "))
no_person = int(input("Enter the charge per unit = "))

total_bill = electricity * charge_per_unit

per_person = (food + rent + total_bill) // no_person

print("Amount per person: ", per_person)


