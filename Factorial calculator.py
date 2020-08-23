#factorial calculator
import math
print("Welcmoe to my Factorial Calculate application")

num = int(input("\nUpto what number you would like to find the factorial for : "))

n = 1
fact = 1
print(num, "! = ",end="")
    #print factorial form
for i in range(1,num+1):
    print(i ,end="")
    if i < num:
        print("*",end="")
    #calculate factorial
while n != num:
    fact = fact * (n+1)
    n = n+1
print("\nfactorial of ", num,"  :  ", fact)

print("#################################################################")
#using math library
print("\nThe factorial of", num, " using maths library : ",end=" ")
print(math.factorial(num))

print("===========================================")

