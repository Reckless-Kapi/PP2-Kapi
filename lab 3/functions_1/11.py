def is_palindrome():
    word = input().replace(" ", "").lower()
    if word == word[::-1]:
        print("It's palindrome")
    else:
        print("It isn't palindrome")

is_palindrome()
