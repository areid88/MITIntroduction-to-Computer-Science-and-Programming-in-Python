# #Write a program that does the following in order:
# 1. Asks the user to enter a number “x”
# 2. Asks the user to enter a number “y”
# 3. Prints out number “x”, raised to the power “y”.
# 4. Prints out the log (base 2) of “x”.

import math

x = int(input("Please input a number: "))
y = int(input("Please input a second number: "))

a = x ** y
print(a)
print(math.log(x, 2))