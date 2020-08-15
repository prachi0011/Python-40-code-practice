#we do multiplication of number
#we do exponent of the number upto 10
#print a message

import math
print("Welcome to my Cool Mathematics Application")
name = input("Your name is : ")
num = float(input("Enter a number(float or integer) to see a magic : "))
message = name + "! Maths is cool."

print()
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

#print table
print("Multiplication Table of ", num, "\n")
for i in range(1, 11):
    print("\t", num, " x ", i, " = ", round(num * i, 1))
print()
print("==================================================")

#print exponent table
print("Exponent table of ", num, "\n")
for i in range(1, 11):
    print("\t", num, "**", i, " = ", round(math.pow(num, i), 1))
print()
print("==================================================")

#print message
print(message.capitalize())
print("\t", message.upper())
print("\t\t", message.lower())
print("\t\t\t", message.title())
print(message.center(60, '@'))

print()
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
