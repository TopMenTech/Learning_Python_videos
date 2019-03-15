# List
l = [1, 2, 3, 4, 5]

# Print entire list
print(l)

# Print first element
print(l[0])

# Print last element
print(l[-1])

# Remove and return last element
print(l.pop())

# Print new list
print(l)

# Common usage, showing multi-line spanning
mylist = ["chicken", 
          "beef",
          "pork", 
          "spam"]
for meat in mylist:
    print("ingredient: " + meat)

# List comprehension
print([item for item in mylist])

# Adding list elements
mylist.append("fish")
print(mylist)

mylist.insert(2, "hamburger")
print(mylist)

# Add lists together
l.extend(mylist)
print(l)

# Delete element
del mylist[2]
print(mylist)
