text = input("Enter a string: ")
uppercase_count = sum(1 for c in text if c.isupper())
lowercase_count = sum(1 for c in text if c.islower())

print("Number of uppercase letters: ", uppercase_count)
print("Number of lowercase letters: ", lowercase_count)
