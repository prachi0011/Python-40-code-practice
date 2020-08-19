#Basketball Roster program

print("Welcome to the Basketball Roster program.\n\n")

#user input
l = []
point_guard = input("Who is your point guard : ").title()
l.append(point_guard)
shooting_guard = input("Who is your shooting guard : ").title()
l.append(shooting_guard)
small_forward = input("Who is your small forward : ").title()
l.append(small_forward)
power_forward = input("Who is your power forward : ").title()
l.append(power_forward)
center = input("Who is your center : ").title()
l.append(center)


print("\n\tYour Stating 5 for the upcoming basketball season")

print(f"\t\tPoint Gaurd: \t\t{l[0]}")
print(f"\t\tshooting Gaurd: \t{l[1]}")
print(f"\t\tSmall Forward: \t\t{l[2]}")
print(f"\t\tPower Forward: \t\t{l[3]}")
print(f"\t\tCenter: \t\t{l[4]}")


#injured person
injured = l.pop(2)
print(f"Oh no! {injured} is injured.")
print(f"Your roster only has {len(l)} players.")
new_center = input("Who will take " + center+ "'s spot: ").title()
l.insert(2, new_center)


#new list ===========================================
print(f"\n\tYour Stating {len(l)} for the upcoming basketball season")

print(f"\t\tPoint Gaurd: \t\t{l[0]}")
print(f"\t\tshooting Gaurd: \t{l[1]}")
print(f"\t\tSmall Forward: \t\t{l[2]}")
print(f"\t\tPower Forward: \t\t{l[3]}")
print(f"\t\tCenter: \t\t{l[4]}")

print(f"Good luck {new_center} you will do great!")
print("Your roster now has 5 players")
