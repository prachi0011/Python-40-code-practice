#prints all factor of the number and also in the form of multiplies
print("Welcome to the factor Generator!")
running = True
while running:
    num = int(input("Enter a number to find the factors: "))
    factors = []
    i = 1
    while i <= num:
        if num  % i == 0:
            factors.append(i)
        i = i + 1
    print(factors)

    for i in factors:
        for j in factors:
            if i * j == num and i < j:
                print(str(i)+ " * " + str(j) + " = " +str( i*  j)) 
    y_n = input("Do you want to run again: ")
    if y_n == 'yes':
        running = True
    else:
        running = False
print("Thanks for using my application!")
