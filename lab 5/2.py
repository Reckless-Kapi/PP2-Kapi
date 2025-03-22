import re

pattern = '^ab{2,3}$'
txt = input()

if re.match(pattern, txt):
    print(f"'{txt}' — Match")
else:
    print(f"'{txt}' — Doesn't match")
