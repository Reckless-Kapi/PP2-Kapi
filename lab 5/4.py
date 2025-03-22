import re

txt = input()
pattern = r'[A-Z][a-z]*$'

if re.fullmatch(pattern, txt):
    print(f"'{txt}' — Match")
else:
    print(f"'{txt}' — Doesn't match")