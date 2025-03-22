import re

txt = input()
pattern = r'a.*b$'

if re.fullmatch(pattern, txt):
    print(f"'{txt}' — Match")
else:
    print(f"'{txt}' — Doesn't match")
