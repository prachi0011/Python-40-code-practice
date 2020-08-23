#fibonacci Series
print("Welcome to the Fibonacci Calculator App,")

digit = int(input("\nHow many digits of the fibonacci Sequence would you like to compute: "))

print("\n======Fibonacci Series using my method=====")
a = 1
b = 1
for i in range(digit):
    if i == 0:
        a = 1
        print(a,end=" ")
    elif i == 1:
        b = 1
        print(b,end=" ")
    else:
        c  = a+b
        a = b
        b = c
        print(c,end=" ")

print("\n\n====================Fibonacci Series using list=====================")
fib = [1, 1]
for i in range(digit-2):
    new_fib = fib[i] + fib[i+1]
    fib.append(new_fib)

for i in fib:
    print(i,end=" ")

#golden ratio
    #example 1/1 2/1 3/2 5/3.....
golden = []
for i in range(len(fib)-1):
    g = fib[i+1]/fib[i]
    golden.append(g)

print("\n\n=================================Golden Numbers===========================")
for i in golden:
    print(i)

print("\nThe ratios of consecutive Fibonacci terms approaches phi 1.68..")
