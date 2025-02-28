import re
from pathlib import Path

file_path = Path("C:/Users/kasym/Documents/Kapi Labs for PP/lab 5/raw.txt")
with file_path.open("r", encoding="utf-8") as file:
    receipt_data = file.read()

def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return ''.join(x.title() for x in components)

snake_case_strings = re.findall(r'\b[a-z]+_[a-z]+\b', receipt_data)
camel_case_converted = [snake_to_camel(s) for s in snake_case_strings]

print(camel_case_converted)
