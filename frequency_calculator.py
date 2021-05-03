#frequecny calculator of letters
from collections import Counter

print("Welcome to Frequency Calculator App.")
string1 = input("Enter a word or phrase to count the frequency: ").lower()

#len of string
t = len(string1)
#letters list contains all alphabets only 
letters = []

for i in string1:
    if i.isalpha():
        letters.append(i)

#total number of alphabets
len_let = len(letters)

letter_count = Counter(letters)
    
    
##print(freq)
##print(ratio)

print("\n\tLetter\t\tOccurence\t\tpercentage")
for value, keys in sorted(letter_count.items()):
    per = (keys * 100) / len_let
    perc = round(per, 2)
    print("\t",value,"\t\t", keys,"\t\t\t", perc,"%")

order_letter_count = letter_count.most_common()
key_phrase_1_ordered_letters = []
for pair in order_letter_count:
    key_phrase_1_ordered_letters.append(pair[0])

print("\nLetters ordered from highest occuence to lowest: ")
for letters in key_phrase_1_ordered_letters:
    print(letters, end='')
