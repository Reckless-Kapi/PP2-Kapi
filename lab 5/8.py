import re

def split_at_uppercase(s):
    return re.findall(r'[A-Z][a-z]*', s)

user_input = input()
print(split_at_uppercase(user_input))
