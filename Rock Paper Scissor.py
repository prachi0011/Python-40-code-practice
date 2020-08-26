#rock paper scissors
import random

print("Welcome to rock paper scissor game.")
rounds = int(input("How many rounds you would like to play: "))

computer = ['rock', 'paper', 'scissor']

#scores of player and computer
com_score = 0
user_score = 0

for i in range(rounds):
    
    print("\nRound :", i+1)
    print(f"Player: {user_score}\tComputer: {com_score}")
    choice = input("Its time to pick one...rock, paper, scissor: ").lower().strip()
    c = computer[random.randint(0,2)]
    print("\tComputer : ", c)
    print("\tPlayer : ", choice)
    if c == choice:
        print("\tIts tie, too boring...")
        print("\tThis round was a tie.")
        
    elif choice != c:
        if choice == 'rock' and c == 'paper':
            com_score += 1
            print("\tPaper covers rocks!")
            print("\tComputer wins round ", i+1)

        elif choice == 'rock' and c == 'scissor':
            user_score += 1
            print("\tRock breaks Scissor!")
            print("\tYou wins round ", i+1)

        elif c == 'rock' and choice == 'paper':
            user_score += 1
            print("\tPaper covers rocks!")
            print("\tYou wins round ", i+1)

        elif choice == 'scissor' and c == 'rock':
            com_score += 1
            print("\tRock breaks scissor!")
            print("\tComputer wins round ", i+1)

        elif choice == 'scissor' and c == 'paper':
            user_score += 1
            print("\tScissor cuts paper!")
            print("\tYou wins round ", i+1)

        elif choice == 'paper' and c == 'scissor':
            com_score += 1
            print("\tScissor cuts paper!")
            print("\tComputer wins round ", i+1)


    elif choice not in computer:
        com_score += 1
        print("This is not a valid option!")
        print("Computer gets the point!!")

#print final result

print("\nfinal Game Results")
print("\tRounds Played: ", rounds)
print("\tPlayer score: ", user_score)
print("\tComputer Score: ", com_score)

if com_score > user_score:
    print("\tWinner: Computer-)")
elif com_score < user_score:
    print("\tWinner: You :-))")
else:
    print("Game tie :-|")
