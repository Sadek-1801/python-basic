spam = ['apples', 'bannanas', 'tofu', 'cats']

def comma_code(items):
  if not items:
    return ''
  if len(items) == 1:
    return items
  
  val = ''
  for word in items: 
    if word == items[-1]:
      val = val + 'and ' + word
    else:
      val = val + word + ', '
  return val

comma_code(spam)