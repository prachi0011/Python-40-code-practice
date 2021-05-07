import random
print("----------------------Power Ball Simulator--------------------")

white_balls = int(input("How many white-balls to draw from for the 5 winning numbers (Normally 69):  "))
if white_balls < 5:
    white_balls =5

red_balls = int(input("How many red-balls to draw from for the Power Ball (Normally 26) :  "))
if red_balls < 1:
    red_balls = 1

odds = 1
for i in range(5):
    odds *= (white_balls - i)
odds *= red_balls/120

print("You have a 1 in " + str(odds) + " chance of winning this lottery. ")

ticket_interval = int(input("Purchase tickets in what interval:  "))

winning_numbers = []
while len(winning_numbers) < 5:
    num = random.randint(1, white_balls)
    if num not in winning_numbers:
        winning_numbers.append(num)
winning_numbers.sort()
num = random.randint(1, red_balls)
winning_numbers.append(num)

#simulate the power ball
print("\n---------------Welcome to the Power Ball-------------------")
print("\nTonight's winning numbers are: ", end="")
for i in winning_numbers:
    print(str(i), end="  ")

input("\nPress 'Enter' to begin purchasing tickets!!!")

tickets_purchased = 0
active = True
tickets_sold = []
while active and winning_numbers not in tickets_sold:
    lottery_num = []
    while len(lottery_num) < 5:
        num = random.randint(1, white_balls)
        if num not in lottery_num:
            lottery_num.append(num)
    lottery_num.sort()
    num = random.randint(1, red_balls)
    lottery_num.append(num)

    if lottery_num not in tickets_sold:
        tickets_purchased += 1
        tickets_sold.append(lottery_num)
        print(lottery_num)

    else:
        print("Losing tickets generated; disgregard..")
        
    if tickets_purchased % ticket_interval == 0:
        print(str(tickets_purchased) + " tickets prchased so far with no winners...")
        choice = input("\nkeep purchasing tickets y/n :  ")
        if choice != 'y':
            active = False

if lottery_num == winning_numbers:
    print("\nWinning ticket numbers:  ", end = "")
    for num in lottery_num:
        print(str(num), end='')
    print("\nPurchased a total of " + str(tickets_purchased) + " tickets")
else:
    print("\n You bought "  + str(tickets_purchased) + " tickets and still lost!")
    print("Better luck next time!")
    
