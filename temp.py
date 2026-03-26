wage = input("Enter the wage: $")
regularHours = input("Enter the regular hours: ")
overTimeHours = input("Enter the overtime hours: ")

wage = float(wage)


REGULAR_PAY = wage * regularHours
OT_PAY = wage * overTimeHours * 1.5

weeklyPay = REGULAR_PAY + OT_PAY
weeklyPay = round(weeklyPay,2)
print("The total weekly pay is $" + str(weeklyPay))