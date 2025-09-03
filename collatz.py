def collatz(number):
  if(number % 2 == 0):
    result = int(number // 2)
    return result
  elif(number % 2 == 1):
    result = int(3 * number + 1)
    return result


try:
  user_input = int(input('Enter an integer: '))

  while user_input != 1:
    user_input = collatz(user_input)
    print(user_input, end=' ')
    
except Exception as err:
  print("An exception happened " + str(err))