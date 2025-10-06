import re
def is_phone_number(text):
  phone_num_pattern = re.compile(r'\d{3}-\d{3}-\d{4}')

  if phone_num_pattern.match(text):
    return True
  else:
    return False

# print('Is 415-555-4242 a phone number?', is_phone_number('415-555-4242'))

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
  segment = message[i:i+12]
  if is_phone_number(segment):
    print('Phone number found: ' + segment)
print('Done')