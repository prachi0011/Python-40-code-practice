#Quadratic Equation Solver
import cmath         #complex maths
print("Welcome to Quadratic Equation Solver Application.")
print("\nA quadratic equation is of the form \"ax^2 + bx + c = 0\"")
print("Your solutions can be real or complex numbers.")
print("A complex number has two parts: a + bj")
print("Where a is the real portion and b is the imaginary portion.")

n = int(input("\nHow many equations would you like to solve today: "))

#get value for first equation

for i in range(n):
    print("\nSolving equation #", i+1)
    print("---------------------------------------------------------------\n")

    #input value of a
    a = float(input("Please enter the value of a (cofficient of x^2): "))
    #input value of b
    b = float(input("Please enter the value of b (cofficient of x): "))
    #input value of c
    c = float(input("Please enter the value of c (constant cofficient): "))

    print(f"\nThe solution for the equation: {a}x^2 + {b}x + {c} = 0 are: ")

    #solving equation
    #value of inside root
    r = (b**2) - 4*a*c
    
    x1 = (-b + cmath.sqrt(r))/(2*a)
    x2 = (-b - cmath.sqrt(r))/(2*a)
    print("\n\tx1 = " + str(x1))
    print("\tx2 = " + str(x2))
    
print("\nThank you for using Quadratic Equation Solver App.")
