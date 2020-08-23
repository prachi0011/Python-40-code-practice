print("Welcome to the Average Calculator App")

name = input("\nEnter your name : ").title()
num = int(input("How many grades would you like to enter : "))
grades =[]
for i in range(num):
    g = float(input("Enter grade: "))
    grades.append(g)

grades.sort(reverse=True)
print(f"\n{name}'s Grades Highest to lowest:")
for i in grades:
    print("\t", i)

print("\n", name, "'s Grade Summary:")
print("\tTotal Number of Grades: ", num)
print("\tHighest Grade: ",grades[0])
print("\tLowest grade: ",grades[num-1])
avg = round(sum(grades)/num)
print("\tAverage: ", round(sum(grades)/num))

desire = float(input("\nWhat is your desired average: "))
next_grade = (desire*(num+1)) - sum(grades)

print("\nGood Luck! ", name)
print("You will need to get a ", round(next_grade), " on your next assignment to earn a ", round(desire)," average.")

print("\nLets see what your average could have been if you did better/worse on an assignment.")
change = float(input("What grade would you like to change: "))
grades.remove(change)
replace = float(input(f"What grade would you like to change {change} to : "))
grades.append(replace)

grades.sort(reverse=True)
print(f"\n{name}'s Grades Highest to lowest:")
for i in grades:
    print(i)

print("\n", name, "'s Grade Summary:")
print("\tTotal Number of Grades: ", num)
print("\tHighest Grade: ",grades[0])
print("\tLowest grade: ",grades[num-1])
new_avg = round(sum(grades)/num)
print("\tAverage: ", round(sum(grades)/num))

print(f"\nYour new Average would be a {new_avg} compared to your real average of {avg}!")
print("That is a change of ", new_avg-avg, " points!")

grades.remove(replace)
grades.append(change)

print("\nToo bad your original grades are still the same!")
print(grades)
print("You should go ask for extra grades")
