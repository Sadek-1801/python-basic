import random



# for i in range(0, 10, 2):
#     print(i)


# for i in range(5, -1, -1):
#     print(i)

# for i in range(5):
#     print(random.randint(1, 10))

# while True:
#     print('Type exit to exit')
#     response = input('>')
#     if response == 'exit':
#         sys.exit()
#     print('You typed ' + response + '.')

secret_number = random.randint(1, 20)
print('I am thinking of a number between 1 and 20')

for guesses_taken in range(1, 7):
    print('Take a guess. ')
    guess = int(input('>>>'))

    if guess < secret_number:
        print('Your Guess is Too Low')
    elif guess > secret_number:
        print('Your Guess is Too high.')
    else:
        break

if guess == secret_number:
    print('Good Job! You got it in ' + str(guesses_taken) + ' guesses!')
else:
    print('Nope. The number was ' + str(secret_number))
