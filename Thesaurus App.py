#Theaurus App
#this program will give you sysnoyms of word


import random

print("Welcome to Thesaurus app.\n")
print("Choose a word from the thesaurus and I will give you a sysnonym.")
print('Thesaurus is a reference book in which words with similiar meanings are grouped together.\n')

word = {'happy': ['pleased', 'glad', 'peaceful', 'sunny', 'delighted'],
        'sad' : ['dark', 'bad', 'unhappy', 'tragic', 'tragic'],
        'life': ['existence', 'survival', 'season', 'living', 'being'],
        'education': ['discipline', 'information', 'improvement', 'study', 'refinement']

    }
print('Here are the words in the thesaurus:')
for key in word.keys():
    print('\t-',key)

w = input("What word you would like to synonym for:").lower()


if w in word.keys():
    r = random.randint(0,4)
    print("A synonym for ", w, " is ", word[w][r] + ".")
else:
    print("I'm sorry!, That word not in thesaurus currently.")


show_all = input("\nWould you like to see whole thesurus(yes/no) : ").lower()

if show_all.startswith('y'):
    for key, values in word.items():
        print("\n", key.title() + " synonyms are: ")
        for value in values:
            print("\t", value)

else:
    print("Hope you enjoy the program")
