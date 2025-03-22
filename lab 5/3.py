import re

txt = input()
pattern = r'^[a-z]+(_[a-z]+)*$'

if re.match(pattern, txt):
    print(f"'{txt}' — Match")
else:
    print(f"'{txt}' — Doesn't match")   