import re
from pathlib import Path

file_path = Path("C:/Users/kasym/Documents/Kapi Labs for PP/lab 5/raw.txt")
with file_path.open("r", encoding="utf-8") as file:
    receipt_data = file.read()

split_at_uppercase = re.findall(r'[A-Z][^A-Z]*', receipt_data)
insert_spaces = ' '.join(split_at_uppercase)

print(insert_spaces)
