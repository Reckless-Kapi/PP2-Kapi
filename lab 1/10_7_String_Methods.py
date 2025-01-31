# capitalize(): Converts the first character to upper case
x = "hello world".capitalize()

# casefold(): Converts string into lower case
x = "HELLO WORLD".casefold()

# center(): Returns a centered string
x = "hello".center(10)

# count(): Returns the number of times a specified value occurs in a string
x = "hello world".count("o")

# encode(): Returns an encoded version of the string
x = "hello".encode()

# endswith(): Returns true if the string ends with the specified value
x = "hello world".endswith("world")

# expandtabs(): Sets the tab size of the string
x = "hello\tworld".expandtabs(4)

# find(): Searches the string for a specified value and returns the position of where it was found
x = "hello world".find("world")

# format(): Formats specified values in a string
x = "My name is {}".format("John")

# format_map(): Formats specified values in a string
x = "{name} is {age} years old".format_map({"name": "John", "age": 30})

# index(): Searches the string for a specified value and returns the position of where it was found
x = "hello world".index("world")

# isalnum(): Returns True if all characters in the string are alphanumeric
x = "hello123".isalnum()

# isalpha(): Returns True if all characters in the string are in the alphabet
x = "hello".isalpha()

# isascii(): Returns True if all characters in the string are ascii characters
x = "hello".isascii()

# isdecimal(): Returns True if all characters in the string are decimals
x = "123".isdecimal()

# isdigit(): Returns True if all characters in the string are digits
x = "123".isdigit()

# isidentifier(): Returns True if the string is an identifier
x = "hello".isidentifier()

# islower(): Returns True if all characters in the string are lower case
x = "hello".islower()

# isnumeric(): Returns True if all characters in the string are numeric
x = "123".isnumeric()

# isprintable(): Returns True if all characters in the string are printable
x = "hello".isprintable()

# isspace(): Returns True if all characters in the string are whitespaces
x = "   ".isspace()

# istitle(): Returns True if the string follows the rules of a title
x = "Hello World".istitle()

# isupper(): Returns True if all characters in the string are upper case
x = "HELLO".isupper()

# join(): Joins the elements of an iterable to the end of the string
x = ",".join(["apple", "banana", "cherry"])

# ljust(): Returns a left justified version of the string
x = "hello".ljust(10)

# lower(): Converts a string into lower case
x = "HELLO".lower()

# lstrip(): Returns a left trim version of the string
x = "   hello".lstrip()

# maketrans(): Returns a translation table to be used in translations
trans = str.maketrans("h", "H")
x = "hello".translate(trans)

# partition(): Returns a tuple where the string is parted into three parts
x = "hello world".partition(" ")

# replace(): Returns a string where a specified value is replaced with a specified value
x = "hello world".replace("world", "there")

# rfind(): Searches the string for a specified value and returns the last position of where it was found
x = "hello hello".rfind("hello")

# rindex(): Searches the string for a specified value and returns the last position of where it was found
x = "hello hello".rindex("hello")

# rjust(): Returns a right justified version of the string
x = "hello".rjust(10)

# rpartition(): Returns a tuple where the string is parted into three parts
x = "hello world".rpartition(" ")

# rsplit(): Splits the string at the specified separator, and returns a list
x = "apple,banana,cherry".rsplit(",")

# rstrip(): Returns a right trim version of the string
x = "hello   ".rstrip()

# split(): Splits the string at the specified separator, and returns a list
x = "apple,banana,cherry".split(",")

# splitlines(): Splits the string at line breaks and returns a list
x = "hello\nworld".splitlines()

# startswith(): Returns true if the string starts with the specified value
x = "hello world".startswith("hello")

# strip(): Returns a trimmed version of the string
x = "   hello   ".strip()

# swapcase(): Swaps cases, lower case becomes upper case and vice versa
x = "Hello World".swapcase()

# title(): Converts the first character of each word to upper case
x = "hello world".title()

# translate(): Returns a translated string
trans = str.maketrans("h", "H")
x = "hello".translate(trans)

# upper(): Converts a string into upper case
x = "hello".upper()

# zfill(): Fills the string with a specified number of 0 values at the beginning
x = "42".zfill(5)
