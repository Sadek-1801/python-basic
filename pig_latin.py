print('Enter the English message to translate into Pig Latin:')
message = input()

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

pig_latin = []
for word in message.split():
  prefix_non_letters = ''
  while len(word) > 0 and not word[0].isalpha():
    prefix_non_letters += word[0]
    word = word[1:]
  if len(word) == 0:
    pig_latin.append(prefix_non_letters)
    continue
  
  # separate the non-letters at the end of this word:
  suffix_non_letters = ''
  while not word[-1].isalpha():
    suffix_non_letters = word[-1] + suffix_non_letters
    word = word[:-1]

  # Remember if the word was in uppercase or title case:
  was_upper = word.isupper()
  was_title = word.istitle()

  word = word.lower() # make sure lowercase for translation:
  
  # separate the consonants at the start of this word:
  prefix_consonants = ''
  while len(word) > 0 and not word[0] in VOWELS:
    prefix_consonants += word[0]
    word = word[1:]
      
  # Add the pig latin ending to the word:
  if prefix_consonants != '':
    word += prefix_consonants + 'ay'
  else:
    word += 'yay'

  # Set the word back to uppercase or title case:
  if was_upper:
    word = word.upper()
  if was_title:
    word = word.title()

  # Add the non-letters back to the start or end of the word.
  pig_latin.append(prefix_non_letters +  word + suffix_non_letters)

print(' '.join(pig_latin))

