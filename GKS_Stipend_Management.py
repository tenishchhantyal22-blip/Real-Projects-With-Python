## Management of GKS monthly stipend
# dormatory fee
# food
# insurance
# Public Transportation
# Mobile Phone Plan
# Personl use

total_stipend = int(input("Enter The Total Stipend Per Month: "))

dormitory_cost = int(input("Enter Monthly Dormitory Cost per month: "))
food = int(input("Enter Food Expenses Per Month: "))
insurance = int(input("Enter Insurance per month: "))
public_transportation = int(input("Enter transportation cost per month: "))
mobile_phone_plan = int(input("Enter mobile phone cost per month: "))
personal_use = int(input("Enter amount for personal use: "))

total_expenses = dormitory_cost + food + insurance + public_tranportation + mobile_phone_plan + personal_use
print("Total expenses per month: ", total_expenses)

saving = tota_stipend - total_expenses
print("Saving: ", saving)





