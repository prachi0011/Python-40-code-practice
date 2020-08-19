#Grocery List
import datetime

time = datetime.datetime.now()  #current date time
month = str(time.month)
day = str(time.day)
hour = str(time.hour)
mint = str(time.minute)
print("Welcome to the Grocery List App.")
print(f"Current Date and Time: {month}/{day}\t {hour}:{mint}")
print("You currently have Meat and Cheese in your list.")
print()

grocery = ['Meat', 'Cheese']
for i in range(3):
    food = input("Type of the food to add to the grocery list: ")
    grocery.append(food.capitalize())

print("Here is your grocery list:")
print(grocery)
grocery.sort()
print()
print("Here is your sorted grocery list :")
print(grocery)

print()
print("Simulating grocery shopping....")
print()

for i in range(len(grocery)):
    print(f"Current grocery list contain {len(grocery)} items : ")
    print(grocery)
    f1 = input("What food you did buy: ")
    grocery.remove(f1.capitalize())
    print(f"Removing {f1.capitalize()} from list...")
    print()

    if(i == 2):
        no_item = grocery.pop()
        print(f"Sorry, the store is out of {no_item}")
        add_new = input("What food would you like instead : ")
        grocery.append(add_new.capitalize())
        print()
        print("Here is what remaining on your grocery list list:")
        print(grocery)
        break
