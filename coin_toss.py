import random
import logging

logging.basicConfig(filename='./log/myProgramLog.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

logging.disable(logging.CRITICAL)
logging.debug('Start the program')


guess = ''
toss = ''
while guess not in ('heads', 'tails'):
    logging.debug('Start of the loop ' + str(guess))
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    logging.debug('End of the loop ' + str(guess))

computer_choice = random.randint(0, 1)  # 0 is tails, 1 is heads
logging.debug(str(computer_choice))

if computer_choice == 1:
    toss = 'heads'
else: 
    toss = 'tails'
    
if toss == guess:
    print('You got it!')
    logging.debug('First Check ' + str(guess) +' ' + str(toss))
else:
    print('Nope! Guess again!')
    logging.debug('First Check Wrong ' + str(guess) + str(toss))
    guess = input()
    logging.debug('Second Check ' + str(guess) + str(toss))
    if toss == guess:
        print('You got it!')
        logging.debug('Second Check Right ' + str(guess) + str(toss))
    else:
        print('Nope. You are really bad at this game.')
        logging.debug('Second Check Wrong ' + str(guess) + str(toss))

logging.debug('End of the Program ' + str(guess) + str(toss))

logging.debug('================================')