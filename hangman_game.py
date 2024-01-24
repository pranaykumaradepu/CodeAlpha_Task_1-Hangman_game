import random

hangman_pics = [ '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''' , '''
    +---+
    O   |
   /|\  |
        |
       ===''','''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
        |
        |
       ==='''
             ]

fruits_list = ['apple', 'banana', 'grapes', 'strawberry', 'orange', 'mango', 'olive', 'kiwi', 'watermelon', 'papaya', 'cherry']

animals_list = ['dog', 'cat', 'rabbit', 'horse', 'cow', 'goat', 'pig', 'chicken', 'duck', 'turkey', 'fish']

programs_list = ['python', 'java', 'c++', 'c#', 'javascript', 'html', 'css', 'php', 'ruby', 'perl', 'assembly']

veggies_list = ['potato','spinach', 'broccoli', 'carrot', 'onion', 'cucumber', 'tomoto', 'lettuce', 'pepper', 'cabbage', 'cauliflower']

softdrinks_list = ['coke', 'pepsi', '7up', 'fanta', 'lemonade', 'orange','juice', 'thumsup','maaza','sting','fizz',]

electronic_list = ['headphones', 'tv', 'laptop', 'phone', 'keyboard', 'camera', 'router', 'computer', 'printer', 'tablet', 'ipad']

lives = 6

u_input = input("Select a topic (fruits, animals, programs, veggies, softdrinks, electronics): ")

topic = u_input.lower()

if topic == "fruits":
    words_list = fruits_list
elif topic == "animals":
    words_list = animals_list
elif topic == "programs":
    words_list = programs_list  
elif topic == "veggies":
    words_list = veggies_list
elif topic == "softdrinks":
    words_list = softdrinks_list
elif topic == "electronics":
    words_list = electronic_list
else:
    print("Please rerun the code and select a valid topic ")
    exit()



chosen_word = random.choice(words_list) # Picks a random word from the words_list to use as the chosen word for the hangman game

word = []
for i in range(len(chosen_word)):
    word += '_'
print(word)
game_over = False
while not game_over:
    guessed_letter = input('Guess A Letter : ')   # asks user to guess a letter from the word
    if guessed_letter.lower() not in 'abcdefghijklmnopqrstuvwxyz':
        print('Please enter a letter')
    elif guessed_letter.lower() in word:
        print('You have already guessed this letter')
    else:
        for l_position in range(len(chosen_word)):
            letter = chosen_word[l_position]
            if letter == guessed_letter.lower():
                word[l_position] = guessed_letter.lower()
        print(word)
        if guessed_letter not in chosen_word:
            lives -= 1
            print(hangman_pics[lives],'\n')
            print(f"remaining lives are {lives}")
            if lives == 0:
                game_over = True
                print('Sorry You Lost The Game Try again')
                print(f'Your word was : {chosen_word}')
                while game_over == True:
                    play_again = input('Do you want to play again? (yes/no): ')
                    if play_again.lower() == 'yes':
                        lives = 6
                        game_over = False
                        chosen_word = random.choice(words_list)
                        word = []
                        for i in range(len(chosen_word)):
                            word += '_'
                        print(word)
                    elif play_again.lower() == 'no':
                        game_over = True
                        print('Thanks for playing')
                        break
                    else:
                        print('Please enter yes or no')
    if '_' not in word:
        game_over = True
        print("Congratulations You Won The Game")
        while game_over == True:
            play_again = input('Do you want to play again? (yes/no): ')
            if play_again.lower() == 'yes':
                lives = 6
                game_over = False
                chosen_word = random.choice(words_list)
                word = []
                for i in range(len(chosen_word)):
                    word += '_'
                print(word)
            elif play_again.lower() == 'no':
                game_over = True
                print('Thanks for playing')
                break

