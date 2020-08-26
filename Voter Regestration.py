#voter registration app
print("Welcome to the Voter Regestation App\n")

name = input("Please enter your name : ").title()

age = int(input("Please enter your age : "))


#list of political parties
parties = ['Republican', 'Peacian', 'Democratic', 'Independency', 'Green']

#list of different message for all paries
msg = ['Major party', 'Aim to Peace in the soceity',
       'Less major party', 'Make yourself free', 'Go green']

if age < 18:
    print("\nYou are not old enough to regester to vote.")
else:
    print("\nCongratulation ", name, "! You are old enough to register to vote.")
    print("\nHere is the list of political parties to join.")
    for p in parties:
        print("\t\t- ",p)
    party = input("\nWhich Party you want to join: ").title()
    for p in range(len(parties)):
        if parties[p] == party:
            print("Congratulations ", name, "!  You have joineed the ", party,"!")
            print(msg[p])
            break
