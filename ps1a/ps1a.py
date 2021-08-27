import math


a = input("Cost of your dream home: ") #total_cost of dream home
total_cost = float(a)
portion_down_payment = total_cost * float(0.25)
b = input("Please enter your annual salary: ") #annual_salary
annual_salary = float(b)
current_savings = annual_salary / 12
r = current_savings * float(0.04)
c = input("Please enter the amount of your salary to be saved: ") #protion_saved
protion_saved = float(c)
monthly_salary = annual_salary/12
end_of_month = r + protion_saved



x = portion_down_payment / end_of_month
y = str(x/12)


print("It will take " + y + "years1 to save your down payment!")