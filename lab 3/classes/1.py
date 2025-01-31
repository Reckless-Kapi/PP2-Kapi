class String:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input("String: ")

    def printString(self):
        print(self.string.upper())

p = String()
p1 = String()
p.getString()
p1.getString()
p.printString()
p1.printString()
