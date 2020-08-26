#Guess my number application

import random
print("Welcome to Guess my number Game\n")
name = input("Hey! What's your name: ").title().strip()
print("Well ", name, "I am thinking number between 1 and 50.\nLets see are able to guess my number or not.")
print("\n$@$@$@$@$@$@$@$@$@$@$@$@$@$@$@$@$@$@$@$@$@$@$@$@$@$@$@\n")
#my number
my_num = random.randint(1, 50)
n = 0
count = 0
while n != my_num:
    n = int(input("Take a guess: "))
    count += 1

    if n < my_num:
        print("Its Too low\n")
    elif n > my_num:
        print("Its Too high\n")
    else:
        print(f"\nGood you have guessed the right number, my nuber is {my_num} and you get it in {count}")
    if count == 5 and n != my_num:
        print("\nWell ", name, " you tried a good, but not guess a right number\nMy number is ",my_num)
        break

