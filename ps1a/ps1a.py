import math


a = input("Cost of your dream home: ") #total_cost of dream home
total_cost = float(a)
down_payment = total_cost * float(0.25)
b = input("Please enter your annual salary: ") #annual_salary
annual_salary = float(b)
current_savings = annual_salary / 12
r = current_savings * float(0.04)
c = input("Please enter the amount of your salary to be saved, as a decimal: ") #protion_saved
protion_saved = current_savings * float(c)
monthly_salary = annual_salary/12
end_of_month = r + protion_saved



x = str(down_payment / end_of_month) # how long it takes to save for the down payment.
#y = str(total_cost - x)
#y = str(x/12)


print("It will take " + x + " months to save your down payment!")
