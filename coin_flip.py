import random

number_of_streaks = 0
experiments = 10000
for experiment_number in range(experiments):
  # Code tha creates a list of 100 'heads' or 'tails' values
  result = [random.choice(['H', 'T']) for _ in range(100)]
  
  # Code that checks if there is a streak of 6 heads of tails in a row
  for i in range(len(result)- 5):
    if result[i:i+6] == ['H', 'H', 'H', 'H', 'H', 'H'] or result[i:i+6] == ['T', 'T', 'T', 'T', 'T', 'T']:
      number_of_streaks += 1
      break

print('Chance of streak: %s%%' % (number_of_streaks / experiments))
print(number_of_streaks)