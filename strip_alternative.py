import re

def strip_letters(string, letters=''):
  if (letters == ''):
    regex = re.compile(r'^\s+|\s+$')
    return regex.sub('', string)
  else:
    replaced_string = re.sub(letters, '', string)
    return replaced_string
  
test1 = strip_letters('  hello world  ')
test2 = strip_letters('helcclo wccorld', 'c')
print(test1)
print(test2)