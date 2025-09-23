import pyperclip
text = pyperclip.paste()

# ToDos
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
text = '\n'.join(lines)
print(text)