# Tuples
t1 = 1, 2, 3, 4
t2 = ("z", "x", "y")
print(t1)
print(t2)

# Sequence unpacking
first, second, third, fourth = t1
print(first)
print(second)
print(third)
print(fourth)
print(t1)

# In-place swapping
mammal = "gorilla"
fish = "mackerel"
mammal, fish = fish, mammal
print(mammal)
print(fish)
