fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits] #Return "orange" instead of "banana"
newlist = [x.upper() for x in fruits] #Set the values in the new list to upper case
newlist = ['hello' for x in fruits] #Set the values in the new list to "hello"
newlist = [x for x in fruits if x != "apple"] #only return items that are not "apple"
newlist = [x for x in fruits] #Return all items
newlist = [x for x in range(10)] #Return 0 to 9
newlist = [x for x in range(10) if x < 5] #Return 0 to 4
