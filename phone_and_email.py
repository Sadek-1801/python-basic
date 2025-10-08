import pyperclip, re

phone_re = re.compile(r'''(
                      (\d{3}|\(\d{3}\))? # area code
                      (\s|-|\.)? # separator
                      (\d{3}) # first 3 digits
                      (\s|-|\.) # separator
                      (\d{4}) # last 4 digits
                      (\s*(ext|x|ext\.)\s*(\d{2,5}))? #  extension
                      )''', re.VERBOSE)

# TODO: Create email regex
email_re = re.compile(r'''(
                      [a-zA-Z0-9._%+-]+  # username
                      @ # @ symbol
                      [a-zA-Z0-9.-]+ #  domain name
                      (\.[a-zA-Z]{2,4}) #  dot-something
                      )''', re.VERBOSE)

# TODO: Find matches in clipboard text
text = str(pyperclip.paste())
matches = []
for groups in phone_re.findall(text):
  phone_num = '-'.join([groups[1], groups[3], groups[5]])
  if groups[6] != '':
    phone_num += ' x' +  groups[6]
  matches.append(phone_num)

for groups in email_re.findall(text):
  matches.append(groups[0])

# TODO: Copy results to the clipboard
if len(matches) > 0:
  pyperclip.copy('\n'.join(matches))
  print('Copied to clipboard:')
  print('\n'.join(matches))
else:
  print('No phone numbers or email addresses found.')





