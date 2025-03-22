import re

pattern = '^ab*$' 

txt = input()

if re.match(pattern, txt):
    print(f"'{txt}' — Match")
else:
    print(f"'{txt}' — Doesn't match")

