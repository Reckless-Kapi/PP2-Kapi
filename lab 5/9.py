import re

def add_spaces(s):
    return re.sub(r'([A-Z])', r' \1', s).strip()

user_input = input()
print(add_spaces(user_input))
