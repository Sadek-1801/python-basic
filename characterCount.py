message = 'It was a devastating day in a scense and enjoyable at the same tiem. Because today Islami Chatra Shibir won in DUCSU election.'

count = {}

for character in message:
  # count.setdefault(character, 0)
  if character == 's':
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)