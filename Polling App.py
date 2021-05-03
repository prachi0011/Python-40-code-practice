#Polling App

print("Welcome to the polling app.\n")

#prompt user input for cause of polling
topic = input("For what reason/ on which topic you want to have a poll: ")
password = input("Set a password for the poll: ")
num_voter = int(input("\nHow many voters you want to participate in your poll: "))

#create a voter database
voters = {}
yes = 0
no = 0

#ask all voters for their result
for i in range(num_voter):
    user_name = input("\nEnter your name: ").title()
    
    if user_name in voters:
        print("You have already given your vote")
        continue;
    
    print("Hello! ", user_name, " today's topic of poll is ", topic)
    vote = input("Your opinion for the poll(yes/no): ").upper()
    voters[user_name] = vote
    if vote == 'YES':
        yes += 1
    else:
        no += 1
    print("Thank you for your vote.")
    voters[user_name] = vote
    
print("\npoll result(yes/no) : ", yes, "/", no)
result = 'YES'
per = 0
if yes > no:
    result = 'YES'
    per = round(yes/num_voter, 2)
elif no > yes:
    result = 'NO'
    per = round(no/num_voter, 2)
else:
    result = 'TIE'
    per = 50.0
print("People max opinion for ", topic, " is ", result, " with percentage ", per)

#ask creater for shoing all result of all people
choose = input("Do you want to see all voters result: ").lower()
if choose == 'yes':
    pas = input("Password of poll: ")

    if pas == password:
        for key, value in voters.items():
            print(key, "\t", value)
    else:
        print("paswword is wrong!, Sorry I acnt let you to see the poll result")
else:
    print("Thank you. Hope you find your answer:-).")
    
