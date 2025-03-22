import re

def camel_to_snake(s):
    return re.sub(r'([A-Z])', r'_\1', s).lower().lstrip('_')

user_input = input("CamelCase: ")
print("snake_case:", camel_to_snake(user_input))
