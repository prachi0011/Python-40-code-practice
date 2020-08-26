#Shipping Accounts Program

print("\nWelcome to the Shipping Accounts Program\n")

acc = ['prachi', 'deepa', 'chiya', 'neha', 'ani']

user = input("hello, What is your username: ").lower()

if user in acc:
    print(f"\nhello, {user}. Welcome back to your account.")
    print("Current shipping prices are as follows: \n")
    print("Shipping orders 0 to 100:\t\t$5.10 each")
    print("Shipping orders 101 to 500:\t\t$5.00 each")
    print("Shipping orders 501 to 1000:\t\t$4.95 each")
    print("Shipping orders over 1000:\t\t$4.80 each")

    item = int(input("How many items would you like to ship: "))
    if item in range(101):
        print(f"To ship {item} items it will cost you {item*5.10} at $5.10 per item.\n")
    elif item in range(101, 501):
        print(f"To ship {item} items it will cost you {item*5.00} at $5.00 per item.\n")
    elif item in range(501, 1001):
        print(f"To ship {item} items it will cost you {item*4.95} at $4.95 per item.\n")
    elif item > 1000:
        print(f"\nTo ship {item} items it will cost you {item*4.80} at $4.80 per item.\n")
    y_n = input("Would you like to place order(y/n): ")
    if y_n.startswith('y'):
        print("Okay! shipping your ", item, "\nTHANK YOU FOR CHECK IN")
    else:
        print("Okay! Your order is not proceeded. \nTHANK YOU FOR CHECK IN")

else:
    print("Sorry you dont have account with us.\n")
    join = input("Would you like to join with us(y/n) :").lower()
    if join.startswith('y'):
        acc.append(user)
        new_user = input("ENter yout first name :").lower()
       
        print(new_user, "\nWelcome to our shop\n")

        print("Current shipping prices are as follows: \n")
        print("Shipping orders 0 to 100:\t\t$5.10 each")
        print("Shipping orders 101 to 500:\t\t$5.00 each")
        print("Shipping orders 501 to 1000:\t\t$4.95 each")
        print("Shipping orders over 1000:\t\t$4.80 each")

        item = int(input("How many items would you like to ship: "))
        if item in range(101):
            print(f"To ship {item} items it will cost you {item*5.10} at $5.10 per item.\n")
        elif item in range(101, 501):
            print(f"To ship {item} items it will cost you {item*5.00} at $5.00 per item.\n")
        elif item in range(501, 1001):
            print(f"To ship {item} items it will cost you {item*4.95} at $4.95 per item.\n")
        elif item > 1000:
            print(f"\nTo ship {item} items it will cost you {item*4.80} at $4.80 per item.\n")
        y_n = input("Would you like to place order(y/n): ")
        if y_n.startswith('y'):
            print("Okay! shipping your ", item, "\nTHANK YOU FOR CHECK IN")
        else:
            print("Okay! Your order is not proceeded. \nTHANK YOU FOR CHECK IN")        
        
        
    
