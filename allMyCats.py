# cat_names = []

# while True:
#   print('Enter the name of cat ' + str(len(cat_names) +  1) + ' (Or Enter nothing to stop.):')
#   name = input()
#   if name == '':
#     break
#   cat_names = cat_names + [name]

# print('The cat names are: ')
# for i in range(len(cat_names)):
#   print(i)

# spam = []
# if spam[0] == 'dog':
#     print('A cat is the first item.')
# else:
#     print('The first item is not a cat.')

spam = 1234
while spam > 0:
  print(spam % 10)
  spam = spam // 10