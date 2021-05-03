from collections import Counter

print("Welcome to Code breaker App.")
string1 = '''
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
        incididunt ut labore et dolore magna aliqua. Egestas erat imperdiet sed euismod
        nisi porta lorem mollis. Sed risus ultricies tristique nulla aliquet enim tortor
        at auctor. Volutpat sed cras ornare arcu dui. Nisi vitae suscipit tellus mauris a
        diam maecenas. Eget nunc lobortis mattis aliquam faucibus purus in. Sit amet volutpat
        consequat mauris nunc congue nisi vitae suscipit. Pulvinar etiam non quam lacus suspendisse
        faucibus. Massa tempor nec feugiat nisl pretium fusce. Dui sapien eget mi proin sed.
        Porttitor eget dolor morbi non arcu risus quis varius quam. Faucibus in ornare quam
        viverra orci sagittis eu volutpat. Id volutpat lacus laoreet non. Viverra suspendisse
        potenti nullam ac tortor vitae purus. Sollicitudin nibh sit amet commodo. Ullamcorper
        a lacus vestibulum sed arcu. Vestibulum lectus mauris ultrices eros in cursus turpis
        massa tincidunt. Vulputate enim nulla aliquet porttitor lacus. Iaculis at erat
        pellentesque adipiscing. Sed ullamcorper morbi tincidunt ornare massa eget.
        qwertyuiopasdfghjklzxcvbnm
        '''
string1 = string1.lower()

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


string2 = '''
        Aliquet eget sit amet tellus cras adipiscing. Vitae justo eget magna fermentum iaculis.
        Aliquam sem fringilla ut morbi tincidunt augue interdum. Nascetur ridiculus mus mauris
        vitae ultricies. Id eu nisl nunc mi ipsum faucibus vitae aliquet. Lorem ipsum dolor sit
        amet consectetur adipiscing. Amet consectetur adipiscing elit duis tristique sollicitudin
        nibh. Habitasse platea dictumst vestibulum rhoncus est pellentesque. Vulputate sapien nec
        sagittis aliquam. Consectetur lorem donec massa sapien. Vitae proin sagittis nisl rhoncus
        mattis. A erat nam at lectus urna. Vel pretium lectus quam id. Velit scelerisque in dictum
        non consectetur a erat. Non diam phasellus vestibulum lorem sed risus ultricies.
        Et pharetra pharetra massa massa ultricies mi quis. qwertyuiopasdfghjklzxcvbnm
        '''
        
string2 = string2.lower()

#len of string
t = len(string2)
#letters list contains all alphabets only 
letters2 = []

for i in string2:
    if i.isalpha():
        letters2.append(i)

#total number of alphabets
len_let1 = len(letters2)

letter_count_1 = Counter(letters2)
    
    
##print(freq)
##print(ratio)

print("\n\tLetter\t\tOccurence\t\tpercentage")
for value, keys in sorted(letter_count_1.items()):
    per = (keys * 100) / len_let1
    perc = round(per, 2)
    print("\t",value,"\t\t", keys,"\t\t\t", perc,"%")

order_letter_count_1 = letter_count_1.most_common()
key_phrase_2_ordered_letters = []
for pair in order_letter_count_1:
    key_phrase_2_ordered_letters.append(pair[0])

print("\nLetters ordered from highest occuence to lowest of second phrase: ")
for letters in key_phrase_2_ordered_letters:
    print(letters, end='')
e_d = input("\n\nDo you want to encode or decode: ")
print('\nEnter a phrase to ' + e_d + ': ', end = " ")
phrase = input().lower()
phrase_list =[]
for i in phrase:
    if i.isalpha():
        phrase_list.append(i)
print(phrase_list)

if e_d == 'encode':
    encoded = ""
    print('Encoding starts...')
    for code in range(len(phrase_list)):
        index1 = key_phrase_1_ordered_letters.index(phrase_list[code])
        encoded = encoded + key_phrase_2_ordered_letters[index1]
       # print(index1 + encoded)
    print(encoded)
else:
    decoded = ""
    print("Decoding starts...")
    for i in range(len(phrase_list)):
        index2 = key_phrase_2_ordered_letters.index(phrase_list[i])
        decoded += key_phrase_1_ordered_letters[index2]
    print(decoded)
