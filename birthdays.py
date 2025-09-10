birthdays = {'sadek': 'Jan 18', 'sakib': 'Apr 26', 'saif': 'Mar 17', 'Mahbuba': 'Feb 26'}

try:
  while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
      break

    if name in birthdays:
      print(birthdays[name] + ' is the birthay of ' + name)
    else:
      print('Enter birthday to update the database')
      bday = input()
      birthdays[name] = bday
      print('Birthday database updated.')
except KeyboardInterrupt:
  print('Keyboard Interrupt happened. Thank you')