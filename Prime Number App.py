#Prime number Application
print("Welcome to the Prime Number Application!")
running = True
while running:
    range_num = int(input("Do want to check only the number you is prime(0) or not  or till the number(1) : "))
    num = int(input("Enter the number : "))
    if range_num == 0:
        n = num
        i = 2
        c = 0
        while i < n:
            if n % i == 0:
                c += 1
                break
            else:
                c = 0
            i += 1
        if c == 0:
            print("Prime Number")
        else:
            print("Not a Prime Number")
    else:
        primes = []
        n1 = num
        while n1 > 1:
            j = 2
            c2 = 0
            while j < n1:
                if n1 % j == 0:
                    c2 += 1
                    break
                else:
                    c2 = 0
                j += 1
            if c2 == 0:
                primes.append(n1)
                print(str(n1) + " is Prime Number")
            else:
                print(str(n1) + " is not prime number")
            n1 -= 1
        print("prime numbers in the range  " + str(num) + " are " + str(sorted(primes)))
    run = input("Do you want to run again: ")
    if run == 'y':
        running = True
    else:
        running = False
