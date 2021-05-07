#python dice app
#Challenge Problem 31

import random
def dice_roll(size, num):
    l = []
    for i in range(num):
        l.append(random.randint(1, size))
    return l
def sum_dice(ar):
    total = 0
    for i in ar:
        total += i
    return total

def  dice_size():
    '''take user input for the  size of dice'''
    size = int(input("How many side would you like to roll on your dice : "))
    return size

def dice_count():
    '''take user input to know how many times dice would roll'''
    num = int(input("How Many dices would you like to roll:  "))
    return num

def roll_again():
    ask = input("\nDo you wanna roll again(y/n): ").lower()
    roll = True
    if ask == 'y':
        roll = True
    elif ask == 'n':
        roll = False
    return roll

def result(dice):
    '''prints the output on dice'''
    print('\nResults are as follow. . . .')
    for i in my_dice:
        print(i)

    
print("Welcome to the Python Dice Application")
r = True
while r:
    size = dice_size()
    num = dice_count()
    my_dice = dice_roll(size, num)
    print("You rolled", num, size, "sided dice")
    result(my_dice)
    print("The total of the values get on your dice is: ", sum_dice(my_dice))
    r = roll_again()

print("Thanks for playing dice roll")
