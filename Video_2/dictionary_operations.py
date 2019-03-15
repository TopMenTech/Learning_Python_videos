# Dictionaries
farm_dict = {"farm": "barn", "stock": [("pig", 1), ("chicken", 4)]}

# Get length
print(len(farm_dict))

# Get item
print(farm_dict["stock"])

# Add item
farm_dict["workers"] = 5
print(farm_dict)

# Increment an item
farm_dict["workers"] += 1
print(farm_dict)

# Item exists?
print("barn" in farm_dict)

# Get all objects
print(farm_dict.items())

# Get only keys
print(farm_dict.keys())

# Get only values
print(farm_dict.values())

# Delete entry
del farm_dict["workers"]
print(farm_dict)

# Iterate over dictionary
for key in farm_dict.keys():
    print(key, farm_dict[key])

