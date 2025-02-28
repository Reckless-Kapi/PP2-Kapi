import re
from pathlib import Path

file_path = Path("C:/Users/kasym/Documents/Kapi Labs for PP/lab 5/raw.txt")
with file_path.open("r", encoding="utf-8") as file:
    receipt_data = file.read()

match_a_followed_by_b = bool(re.search(r'\ba[b]*\b', receipt_data))

print(match_a_followed_by_b)
