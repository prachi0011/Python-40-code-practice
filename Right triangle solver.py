#Right Triangle Solver
import math

print("Welcome to my Right Triangular Solver")
print()

first = float(input("Enter the first leg of triangle : "))
second = float(input("Enter the second leg of triangle : "))

#calculate hypotenuse
hypo = math.pow((math.pow(first, 2) + math.pow(second, 2)), 0.5)

#calulate perimeter
perimeter = first + second + hypo

#calculate area
area = round(((first * second) / 2), 3)

print()
print("*****************************************")
print()

#print hypotenuse
print("Hypotenuse of the triangle = ", round(hypo, 3))

#print perimeter
print("Perimeter of the triangle = ", round(perimeter, 3))

#print area
print("Area of the triangle = ", area)

print()
print("*****************************************")
