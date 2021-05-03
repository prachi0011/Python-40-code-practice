print("Welcome to even odd number sorter application")
running = True
while running:
    num_string = input("Enter a string of number seperated by comma: ")
    num_string = num_string.replace(' ' , '')
    nums = num_string.split(',')

    even = []
    odd = []
    for i in nums:
        if int(i) % 2 == 0:
            even.append(int(i))
            print(i + " is even.")
        else:
            odd.append(int(i))
            print(i + " is odd.")
    print("here is sorted even number")
    print(sorted(even))
    print("Here is sorted odd numbers")
    print(sorted(odd))

    y_n = input("Do you want to run program y/n: ")
    if y_n == 'y':
       running = True
    else:
        running = False
