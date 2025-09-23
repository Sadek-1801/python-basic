import pyperclip

text = pyperclip.paste()
alt_text = ''
make_upcase = False
for character in text:
  if make_upcase:
    alt_text += character.upper()
  else: 
    alt_text += character.lower()
  
  make_upcase = not make_upcase

pyperclip.copy(alt_text)
print(alt_text)