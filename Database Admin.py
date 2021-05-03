#Database Admin

print("Welcome to the database Admin")

user = input("\nUsername: ")

data = {
    'prachi01' : 'Pr@chi014',
    'bob123' : 'B0bby234',
    'akiyan00' : '012345678',
    'preeti89' : '89iteerp',
    'admin11' : 'Admin001'
    }

if user in data.keys():
    if user == 'admin11':
     password = input("Password: ")
     if password == data[user]:
        print("\nHello admin!, logged in!")
        print("\nHere is the current user database:")
        for key, values in data.items():
            print("\tUsername: ", key, end="\t")
            
            print("Password: ", values)
    else:
        password = input("Password: ")  #password input
        if password == data[user]:
            print("\nYou are logged in!")
            change_pass = input("Do you want to change your password(yes/no): ").lower()
            if change_pass == 'yes':
                new_pass = input("New Password: ")
                if len(new_pass) >= 8:
                    print("\nYour password has been updated.")
                    data[user] = new_pass

                else:
                    print("\nYour password will not change.")
                print(user, " your password is ", data[user])
            else:
                print("\nThank You!!")
        else:
            print("Wrong password")

else:
    print("\nuser not found in admin database.")
