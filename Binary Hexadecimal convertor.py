#binary conversion

print("Welcome to the Binary/HExadecimal Convertor App")

#user input
max_value = int(input("\nCompute binary and hexadecimal values upto the following decimal number: "))
decimal = list(range(1, max_value+1))

binary = []
hexadecimal =[]

for num in decimal:
    binary.append(bin(num))
    hexadecimal.append(hex(num))

print("\nGenerating Lists....complete!")
print("\nUsing slices, we will now show a portion of each list.")
start = int(input("What decimal number would you like to start at: "))
stop = int(input("What decimal number would you like to stop at: \n"))


print()
print("Decimal values from", start, " to ", stop)
for n in decimal[start:stop+1]:
    print(n)
#print binary values
print()
print("Binary values from", start, " to ", stop)
for b in binary[start:stop+1]:
    print(b)
#print hex values
print()
print("Hexadecimal values from", start, " to ", stop)
for h in hexadecimal[start:stop+1]:
    print(h)

input(f"\nPress Enter to see all values values ffrom 1 to{max_value}")
print("Decimal----------Binary---------Hexadecimal")
print("============================================")
for n, b, h in zip(decimal, binary, hexadecimal):
    print(n, "\t||\t", b, "\t\t||\t", h)
