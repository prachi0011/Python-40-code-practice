#calculator
import math
def addition(a, b):
    '''addtion of two num'''
    add = round(a + b, 2)
    print("The sum of", a, 'and', b, 'is', add)
    return add


def subtraction(a, b):
    '''subtraction of two num'''
    sub = round(a - b, 2)
    print("The subtraction of", a, 'and', b, 'is', sub)
    return sub
    
def multipication(a, b):
    '''multiply of two numbers'''
    mul = round(a * b, 2)
    print("The multipication of", a, 'and', b, 'is', mul)
    return mul

def division(a, b):
    '''a divided by b'''
    if b == 0:
        return 'Can not divide by zero'
    else:
        div = round(a / b,2)
        print("The division of", a, 'and', b, 'is', div)
    return div

def exponatation(a, b):
    '''a to the power b'''
    ex = round(math.pow(a, b), 2)
    print("The result of", a, 'raised to the', b, 'power is', ex)
    return ex

def history(operations):
    '''after doing all calculations it will print out all the calculations done'''
    print("\nCalculation Summary:")
    for x in operations:
        if type(x) != str:
            print(str(x[0]) + '  ' + str(x[2]) +'  ' + str(x[1]) + ' = ' + str(x[3]))
        else:
            print(x)
       
        
    
def calculate_more():
    '''ask user to do more calculations'''
    y_n = input("Do want to perform more calculation(y/n):  ")
    if y_n == 'y':
        return True
    else:
        return False

def user_input():
    value = float(input("Enter a value:  "))
    return value

def perform_calculation(a, b):
    '''it will ask user what calculation you want to perform'''
    perform = input("\nEnter a operation('addition(+)', 'subtraction(-)', 'multiply(*)', 'divide(/)', 'exponential(^)'):  ")
    if perform == '+':
        result = addition(a, b)
        
    elif perform == '-':
        result = subtraction(a, b)
        
    elif perform == '*':
        result = multipication(a, b)
        
    elif perform == '/':
        result = division(a, b)
        if type(result) == str:
            print(result)
            return 'DIV ERROR'
    elif perform == '^':
        result = exponatation(a, b)
        
    else:
        print('Invalid Operation, TRY AGAIN')
        return 'OOP ERROR'
    return [a, b, perform, result]
    
    
print('Welcome to python calculator!!')
#print(calculate_more())
performing = True
operation = []
while performing:
    print('Enter the two numbers and then choose the desired operation')
    a = user_input()
    b = user_input()
    result = perform_calculation(a,b)
    operation.append(result)
    performing = calculate_more()
history(operation)
print('Thank you for using The Python Calculator App.\tGoodbye.')
