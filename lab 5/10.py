import re
from pathlib import Path

# Путь к файлу (используем raw-строку или заменяем обратные слэши)
file_path = Path(r"C:\Users\kasym\Documents\Kapi Labs for PP\lab 5\raw.txt")
with file_path.open("r", encoding="utf-8") as f:
    text = f.read()

# Регулярное выражение:
# \b - граница слова
# (?:[A-Z][a-z]+|[A-Z]{2,}) - слово, которое либо начинается с заглавной и продолжается строчными,
# либо полностью заглавное (2 и более символа)
# (?:\s+(?:[A-Z][a-z]+|[A-Z]{2,}))* - ноль или более слов, разделённых пробелом, удовлетворяющих тому же условию
pattern = r'\b(?:[A-Z][a-z]+|[A-Z]{2,})(?:\s+(?:[A-Z][a-z]+|[A-Z]{2,}))*\b'

matches = re.findall(pattern, text)

def to_snake(s):
    # Преобразует группу слов в snake_case, разделяя по пробелам и переводя в нижний регистр
    return '_'.join(s.split()).lower()

# Преобразуем все найденные совпадения в snake_case
snake_names = [to_snake(match) for match in matches]

# Задаем список исключений (те совпадения, которые не являются нужными брендами)
exclude = {"europharma", "naturella", "aura", "rx", "webkassa", "kz"}

# Фильтруем список
filtered = [name for name in snake_names if name not in exclude]

# Удаляем дубликаты, сохраняя порядок
unique_filtered = []
seen = set()
for name in filtered:
    if name not in seen:
        unique_filtered.append(name)
        seen.add(name)

print(unique_filtered)
