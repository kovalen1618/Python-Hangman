import random
import string
from words import words
from lives_visual_dict import lives_visual_dict

# We have to create a function to get only valid words
def get_valid_word(words):
  word = random.choice(words) # Randomly chooses something from the words list
  # This loop will keep iterating until we get a valid word (a word that isn't a space or a dash)
  while '-' in word or ' ' in word: 
    word = random.choice(words)

  return word.upper()

def hangman():
  word = get_valid_word(words)
  word_letters = set(word) # Letters in the word
  alphabet = set(string.ascii_uppercase)
  used_letters = set() # What the user has guessed
  lives = 6

  # Getting user input
  while len(word_letters) > 0 and lives > 0: # len = length
    # Letters used
    # ' '.join(['a', 'b', 'cd']) --> a b cd
    print('You have', lives, 'lives left and you have used these leters: ', ' '.join(used_letters))

    # What current word is (ie W - R D)
    word_list = [letter if letter in used_letters else '-' for letter in word]
    print(lives_visual_dict[lives]) # Shows image based off index in dictionary
    print('Current word: ', ' '.join(word_list))

    user_letter = input('Guess a letter: ').upper() # Put to uppercase to pass equality conditionals
    if user_letter in alphabet - used_letters:
      used_letters.add(user_letter)
      if user_letter in word_letters:
        word_letters.remove(user_letter)
      
      else:
        lives = lives - 1 # Takes away a life if wrong
        print('Letter is not in word.')
      
    elif user_letter in used_letters:
      print('You have already used that character. Please try again.')

    else:
      print('Invalid character. Please try again.')

  # Gets here when len(word_letters) == 0 OR when lives == 0
  if lives == 0:
    print(lives_visual_dict[lives])
    print('You died. The word was', word)
  else:
    print('You guessed the word', word, '!!')

hangman()

