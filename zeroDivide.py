def spam(devide_by):
  try:
    return 42 / devide_by
  except ZeroDivisionError:
    print('Error: Invalid argument.')

print(spam(2))
print(spam(1))
