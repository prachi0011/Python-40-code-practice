#different types of list

print("Hey! Welcome to the progra. Here you come to know about different types of list in python")

#different types of list
l1 = [2, 4, 6, 7]       #all integer
l2 = [2.0, 4.4, 6.6, 8.88]      #all float
l3 = ['a', 'd', 'c', 'z', 'q']      #all string
l4 = [[1, 2], [2, 4], [3,6]]        #list
l5 = [('hello'), (2, 3, 4), ('a', 'b')]     #all tuple
l6 = [{2, 4, 6}, {'a', 'b'}]        #all set
l7 = [{1:'a', 2:'b', 3:'c'}, {'p':11, 'q':22, 'r':33}]  #alldict
l8 = [11, 22.22, 'Prachi', [2, 'abc', 4.5], (2, 5, 6), {2, 20, 200}, {'p':11, 'q':22, 'r':33}]

print()
print("######################################################################")
print()
print()

#print list with datatypes
print("The first list  l1 contain elements : ", l1)
print("Type of all elements of l1 is : ", type(l1[0]))
print()

print("The second list  l2 contain elements : ", l2)
print("Type of all elements of l2 is : ", type(l2[0]))
print()

print("The third list  l3 contain elements : ", l3)
print("Type of all elements of l3 is : ", type(l3[0]))
print()

print("The fourth list  l4 contain elements : ", l4)
print("Type of all elements of l4 is : ", type(l4[0]))
print()

print("The fifth list  l5 contain elements : ", l5)
print("Type of all elements of l5 is : ", type(l5[0]))
print()

print("The sixth list  l6 contain elements : ", l6)
print("Type of all elements of l6 is : ", type(l6[0]))
print()

print("The seventh list  l7 contain elements : ", l7)
print("Type of all elements of l7 is : ", type(l7[0]))
print()

print("The first list  l8 contain elements : ", l8)
print()
for i in l8:
    print("Element of list l8 ", i, " with type ", type(i))

s1 = sorted(l1)
print("The sorted list l1(which contain all integer) : \n", s1)
s2 = sorted(l3)
print("the sorted string list :\n", s2)

print()
print()
print("######################################################################")
