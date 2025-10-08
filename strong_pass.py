# import re

# def strong_pass(password):
#   # at least 8 characters
#   # uppercase and lowercase letters
#   # at least one digits

#   regex = re.compile(r'^(?=.*[a-zA-Z0-9]).{8,}$')
#   if (regex.match(password)):
#     return True
#   else:
#     return False

# print(strong_pass('<PASSWORD>'))
# print(strong_pass('Password123'))
# print(strong_pass('pasass123'))

import re

# Original (correct) pattern
original_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$'

# Your proposed pattern
proposed_pattern = r'^(?=.*[a-zA-Z0-9]).{8,}$'

def test_password(pattern, password):
    return bool(re.match(pattern, password))

# Test cases
test_cases = [
    "Password123",    # Should be valid - has upper, lower, digit
    "password123",    # Should be invalid - missing uppercase
    "PASSWORD123",    # Should be invalid - missing lowercase
    "Password",       # Should be invalid - missing digit
    "Pass123",        # Should be invalid - less than 8 chars
    "ABCDefgh",       # Should be invalid - missing digit
    "!@#$%^&*()1Aa",  # Edge case with special chars
]

print("Password    | Original | Your Pattern")
print("-" * 35)
for pwd in test_cases:
    orig_result = test_password(original_pattern, pwd)
    prop_result = test_password(proposed_pattern, pwd)
    print(f"{pwd:<12} | {orig_result}      | {prop_result}")
