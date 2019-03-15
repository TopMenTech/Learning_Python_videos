# String operations

# Different quotes
print("This is 'a' string.")

# Same quotes
print("This is a \"different\" string.")

# Concatentation
print("abc" + "zyx")

# Multiple copies
print("Spam!" * 3)

# Convert integer to string
print(str(3))

# Iteration
occupation = "I'm a lumberjack"
for letter in occupation:
    print(letter)

# Iteration on same line
for letter in occupation:
    print(letter, end="")

# Indexing
print(occupation[0])
print(occupation[2])
print(occupation[-1])

# Slicing
print(occupation[1:3], occupation[4:], occupation[:-1])

# String formatting (legacy)
sandwich = "spam"
quantity = 7

print("Please give me %d %s sandwiches." % (quantity, sandwich))

# String formatting (current)
# relative position substitution
print("Please give me {} {} sandwiches.".format(quantity, sandwich))

# numbered position substitution
print("Please give me {0} {1} sandwiches.".format(quantity, sandwich))

# keyword substitution
print("Please give me {number} {type} sandwiches.".format(number=quantity, type=sandwich))

# f-string
print(f"Please give me {quantity} {sandwich} sandwiches.")

# Joining strings
string1 = "a b c"
string2 = "3 2 1"
string3 = string1 + string2
print(string3)
string4 = string2.join(string1)
print(string4)

new_string = ("1a", "2b", "3c")
print("-".join(new_string))

# Splitting strings
splitter = "Judean People's Front"
print(splitter.split())
another_splitter = "A, B, C"
print(another_splitter.split(","))

