#Grade calculation application

print("Welcome to Grade Calculation Application")
name = input("Enter your name : ")
print()

print("Enter your grades between 1 and 100")
#input grades
g1 = int(input("Enter your first grade(as integer) : "))
g2 = int(input("Enter your second grade(as integer) : "))
g3 = int(input("Enter your third grade(as integer) : "))
g4 = int(input("Enter your fourth grade(as integer) : "))
g5 = int(input("Enter your fifth grade(as integer) : "))

gradelist = list([g1, g2, g3, g4, g5])
print(name, ", your grades are: ", gradelist)
print()

#print sorted grades
htol = list()
a = gradelist[0];
for i in gradelist:
    if i > a:
        htol.append(a)
        a = i
print(name, ", your grades from highest to lowest are : ", htol)
print()

#lowest grade
low = min(gradelist)
print("Lowest grade : ", low)
#highest grade
high = max(gradelist)
print("Highest grade : ", high)
print()

#total of grades
print("The total of your grades : ", sum(gradelist))
#average
print("Average of your grades : ", sum(gradelist)/5)

print("The lowest two grades will now be dropped.")
fd = gradelist.remove(low)
print("The first removed grade : ", low)
low2 = min(gradelist)
sd = gradelist.remove(low2)
print("The second removed grade : ", low2)

print()
print("Your remaing scores are : ", gradelist)
print("The sum of your grades are dropping to grades : ", sum(gradelist))
print("The average of your grades are dropping to grades : ", sum(gradelist)/3)

print()
print("Nice work! ", name)




