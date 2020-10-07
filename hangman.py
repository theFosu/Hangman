# libraries
import random

# Asks for the name of the player and inserts it into the <username> variable
username = input('Welcome to group 70\'s game of hangman! What\'s your name? ')

# list of random words to select from
wordlist = ['potato', 'tomato']

# picks a random word and stores it into <correct>
correct = wordlist[random.randrange(len(wordlist))]

# guessed letters
guessed = []

# wrong answers counter
wrong = 0

# loop to make the game work
while True:

    # Number of missing letters
    missing = 0

    # formatting
    print('')
    
    # Loop for each character in the word
    for correct_char in correct:
    
        # checks whether the character is contained in the list of guessed words
        if correct_char in guessed:
        
            # prints the guessed character
            print (correct_char, end='')
        else:
            # prints an underscore in the place of an unknown character
            print ('_', end='')
            
            missing += 1
    
    print('')
    
    # if there's no more letters missing
    if missing == 0:
        retry = input('\nYou have won! \nDo you want to play again? ')
        # If player wants to retry
        if retry == 'yes':
        
            # Resets all parameters
            correct = wordlist[random.randrange(len(wordlist))]
            guessed = []
            wrong = 0
        else:
            break
        
    
    # Asks for the letter and stores it in trial
    trial = input('\nCome on, ' + username + '! Try to guess a letter: ')
    
    # Checks whether the character is valid and not already inserted
    if len(trial) == 1 and trial.isalpha() and trial not in guessed:
        if trial in correct:
            # Adds the trial to the guessed
            guessed.extend(trial.lower())
        else:
            # increseas the wrong letter counter
            wrong += 1
            if wrong == 1:
                print('____________\n|          |\n|          O\n|\n|\n|\n|_____')
            if wrong == 2:
                print('____________\n|          |\n|          O\n|          |\n|\n|\n|_____')
            if wrong == 3:
                print('____________\n|          |\n|          O\n|         _|\n|\n|\n|_____')
            if wrong == 4:
                print('____________\n|          |\n|          O\n|         _|_\n|\n|\n|_____')
            if wrong == 5:
                print('____________\n|          |\n|          O\n|         _|_\n|          /\n|         /\n|_____')
            if wrong == 6:
                print('____________\n|          |\n|          O\n|         _|_\n|          /\\ \n|         /  \\\n|_____')
                
                retry = input('\nYou have lost! The correct word was ' + correct + '\nDo you want to play again? ')
                # If player wants to retry
                if retry == 'yes':
                
                    # Resets all parameters
                    correct = wordlist[random.randrange(len(wordlist))]
                    guessed = []
                    wrong = 0
                else:
                    break
                
    else:
        print('\nIllegal value!')