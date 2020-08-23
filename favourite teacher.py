#favourite teacher

print("Welcome to the Favourite teacher Application.\n")
teach = []
t1 = input("Enter your first favourite teacher : ").title()
teach.append(t1)
t2 = input("Enter your second favourite teacher : ").title()
teach.append(t2)
t3 = input("Enter your third favourite teacher : ").title()
teach.append(t3)
t4 = input("Enter your fourth favourite teacher : ").title()
teach.append(t4)

print("\nHere is your list of favourite teachers : ")
print(teach)
print("Alphabetically sorted list of teachers : ")
teach.sort()
print(teach)
print("Reverse alphabetically sorted of teachers : ")
teach.sort(reverse=True)
print(teach)

print(f"\nYour two top teachers are : {t1} and {t2}")
print(f"Your next two top teachers are : {t3} and {t4}")
print(f"Your last favourite teacher is : {t4}")
print("You have a total of ",len(teach), " favourite teachers.")
t5 = input(f"\nOops, {t1} is no longer your first favourite teacher. Who is your new FAVOUTITE teacher :").title()

teach.insert(0, t5)
print("\nHere is your list of favourite teachers : ")
print(teach)
print("Alphabetically sorted list of teachers : ")
teach.sort()
print(teach)
print("Reverse alphabetically sorted of teachers : ")
teach.sort(reverse=True)
print(teach)

print(f"\nYour two top teachers are : {t5} and {t1}")
print(f"Your next two top teachers are : {t2} and {t3}")
print(f"Your last favourite teacher is : {t4}")
print("You have a total of ",len(teach), " favourite teachers.")

rt = input(f"\nYou've decided you no longer like a teacher. Which teacher would you like to remove from your list: ").title()
#for i in teach:
#    if rt == i:
teach.remove(rt)


print("\nHere is your list of favourite teachers : ")
print(teach)
print("Alphabetically sorted list of teachers : ")
teach.sort()
print(teach)
print("Reverse alphabetically sorted of teachers : ")
teach.sort(reverse=True)
print(teach)

print(f"\nYour two top teachers are : {t1} and {t2}")
print(f"Your next two top teachers are : {t3} and {t4}")
print(f"Your last favourite teacher is : {t4}")
print("You have a total of ",len(teach), " favourite teachers.")
