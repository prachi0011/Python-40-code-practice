#import random
import random
print("Welcome to the Guess The Word Game")

game_dict= {
                'sports' : ['football', 'baseball', 'cricket', 'badminton', 'tennis'],
                'fruits' : ['apple', 'mango', 'banana', 'grapes', 'watermelon', 'guava'],
                'color' : ['pink', 'red', 'yellow', 'black', 'blue', 'white', 'gray', 'voilet'],
                'subjects' : ['english', 'automata', 'networks', 'mathematics', 'hindi', 'science'],
                'programming languages' : ['python', 'c', 'java', 'scala', 'php', 'cpp', 'javascript', 'swift']
                }

categories  = []
for key in game_dict.keys():
    categories.append(key)
playing = True
while playing:
    game_category = categories[random.randint(0, (len(categories)-1))]
    guess_word = game_dict[game_category][random.randint(0, (len(game_dict[game_category])-1))]

    print("Guess " + str(len(guess_word)) + " letters word from the category of " + game_category)
    string = []
    for i in range(len(guess_word)):
        print('_', end = '')
        string.append('_')
    s = ''.join(string)
    count = 0
    while s != guess_word:
        user_input = input("\nGuess the word : ").lower()
        count += 1
        for i in range(len(user_input)):
            if user_input[i] in guess_word :
               if guess_word.find(user_input[i], i, len(guess_word)) >= 0:
                   string[guess_word.find(user_input[i], i, len(guess_word))] = user_input[i]

        s = ''.join(string)
        print(s)
    if count == 1:
        print("YAY! You got it in just one guess")
    else:
        print("You guess the word in " +str(count) + " guesses.")
    y_n = input("\nDo you want to play again(y/n): ").lower()
    if y_n == 'y':
        playing = True
    else:
        playing = False
