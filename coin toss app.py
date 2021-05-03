#coin toss
import random
print("Welcome to coin toss")

n = int(input("How many time you would like to toss : "))
see = input("Would you like to see thr result of each flips:").lower()


h = 0
t = 0
for i in range(n):
    c = random.randint(1,2)
   # print(t)
    if c == 1:
        h += 1
        if see.startswith('y'):
            print('HEAD')
    elif c == 2:
        t += 1
        if see.startswith('y'):
            print('TAIL')
        
    if h == t:
        print("At ", i+1, " head and tail are equal count")
                            
h_per = round(100*h/n, 2)
t_per = round(100*t/n, 2)
print("\nResults of flipping A coin ", n, "Times:\n")
print("\nSide\tCount\tPercentage")
print(f"Heads\t{h}/{n}\t{h_per}")
print(f"Tails\t{t}/{n}\t{t_per}")
