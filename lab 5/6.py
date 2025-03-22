import re

txt = input()
pattern = r'[ ,.]'

result = re.sub(pattern, ':', txt)
print(result)
