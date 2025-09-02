def collatz(number):
  if(number % 2 == 0):
    result = int(number // 2)
    print(result)
    return result
  elif(number % 2 == 1):
    result = int(3 * number + 1)
    print(result)
    return result

