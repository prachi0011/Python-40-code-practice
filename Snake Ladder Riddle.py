#Snake Ladder Riddle
import random

print("Welcome to Snake&Ladder Riddle game.")
print("In this you found one intersting way of laddering up and snaking down!")
name = input("Enter your name: ")

print("*********************************************************************************")
input("\nLets get start the game, press ENTER to start.")

#reach point
reach = 100
user_count = 1
com_count = 1

dice1 = 0
dice2 = 0
winner = "unkown"

while dice1 != 6 or dice2 != 6:
    print("\nYour turn")
    print("you are at ", user_count)
    input("Hit enter for your turn")
    dice1 = random.randint(1, 6)
    print("Dice: ", dice1)
    if dice1 == 6:
        user_count += 1
        print("You are now on the way....")
        break
    
    input("Hit Enter")
    print("\ncomputer turn")
    print("Computer is at ", com_count)
    dice2 = random.randint(1, 6)
    print("Dice: ",dice2)
    if dice2 == 6:
        com_count += 1
        print("Computer is now on the way....\n")
        break

#ladders and theri reaching point
ladder = {2:38, 4: 14, 9:31, 33: 85, 52: 88, 80: 99}
#snakes and their reaching point
snake = {97: 8, 92: 53, 62: 55, 56: 15, 51: 11}


#second loop for moving on the path
while com_count != reach or user_count != reach:
    dice1 = random.randint(1, 6)
    user_count += dice1
    dice2 = random.randint(1, 6)
    com_count += dice2

    input("\nHit ENTER for your dice")
    print("Dice: ", dice1)
    print("\n\t$$$$$$$$$$$$$$$$$$$$$$$$")
    print("\tYour Destination: ", user_count)
    print("\t$$$$$$$$$$$$$$$$$$$$$$$$\n")
    if dice1 == 6:
        input("Its Your turn again")
        dice1 = random.randint(1,6)
        print("Dice: ", dice1)
        user_count += dice1
        print("\n\t$$$$$$$$$$$$$$$$$$$$$$$$")
        print("\tYour Destination: ", user_count)
        print("\t$$$$$$$$$$$$$$$$$$$$$$$$\n")
        
    #user reached up to ladder
    if user_count in ladder:
        user_count = ladder[user_count]
        print("Yuyyy!! you moved up to a ladder and you are now at ", user_count)

    #snake bites user
    if user_count in snake:
        user_count = snake[user_count]
        print("Ooonooo!! you moved down with a snake and you are now at ", user_count)
        
    if user_count >= reach:
        winner = name.upper()
        break

    #computer turn
    input()
    print("\nComputer Turn")
    print("Dice: ", dice2)
    print("\n\t$$$$$$$$$$$$$$$$$$$$$$$$")
    print("\tComputer Destination: ", com_count)
    print("\t$$$$$$$$$$$$$$$$$$$$$$$$\n")
    if dice2 == 6:
        print("Its compute turn again")
        dice2 = random.randint(1,6)
        com_count += dice2
        print("\n\t$$$$$$$$$$$$$$$$$$$$$$$$")
        print("\tcomputer Destination: ", com_count)
        print("\t$$$$$$$$$$$$$$$$$$$$$$$$\n")

    #computer ladder up
    if com_count in ladder:
        com_count = ladder[com_count]
        print("Yuyyy!! computer moved up to a ladder and you are now at ", user_count)

    #computer bitten by snake
    if com_count in snake:
        com_count = snake[com_count]
        print("Ooonooo!! computer moved down with a snake and you are now at ", user_count)
    
    if com_count >= reach:
        winner = "COMPUTER"
        break

#winner
print("\n\n\t@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
print("\t\t", winner)
print("\n\t@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    

    

    
