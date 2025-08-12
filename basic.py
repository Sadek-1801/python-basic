# while True:
#   print ('Who are you?')
#   name = input('> ')
#   if name != 'Joe':
#     continue
#   print('Hello, Joe. What is the password? (It is a fish.)')
#   password = input('>')
#   if password == 'swordfish':
#     print('Access granted.')
#     break

name = ''
while not name:
  print('Enter your name')
  name = input('>')
  print('How many guests will you have?')
  num_of_guests = int(input('>'))
  if num_of_guests:
    print('please be prepared for {num_of_guests}')
  print('Done! You have completed.')