def to_camel(snake):
    parts = snake.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

user_input = input("snake_case: ")
print("CamelCase:", to_camel(user_input))
