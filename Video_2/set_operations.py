# Sets
set1 = {"airplane", "pilot", "wheels", "wing", "engine"}
set2 = {"airport", "airplane", "fuel"}

# Return True if set1 has no common elements w/ set2
print(set1.isdisjoint(set2))

# Return True if all elements of set1 are in set2
print(set1.issubset(set2))

# Return True if set1 is true subset of set2 but not equal
print(set1 < set2)

# Return True if every element of set2 is in set1
print(set1.issuperset(set2))

# Return True if set1 is true superset of set 2 but not equal
print(set1 > set2)

# Return new set that includes elements of all sets
print(set1.union(set2))

# Return new set with all common elements of given sets
print(set1.intersection(set2))

# Return new set with all elements that exist in set1 but no others
print(set1.difference(set2))

# Return new set with elements that are unique to each set
print(set1.symmetric_difference(set2))

# Return a new set with a copy of elements from given set
print(set1.copy())
