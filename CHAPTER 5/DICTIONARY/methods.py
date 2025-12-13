# Original dictionary
d = {"name": "Sumit", "age": 20}

print("Original dict:", d)
print("Type:", type(d))
print()

# copy()
d_copy = d.copy()
print("Copy:", d_copy)

# get()
print("Get age:", d.get("age"))
print("Get marks (default):", d.get("marks", 0))

# setdefault()
d.setdefault("city", "Delhi")
print("After setdefault:", d)

# update()
d.update({"age": 21, "course": "AI"})
print("After update:", d)

# keys(), values(), items()
print("Keys:", d.keys())
print("Values:", d.values())
print("Items:", d.items())

# pop()
removed_age = d.pop("age")
print("Popped age:", removed_age)
print("After pop:", d)

# popitem()
last_item = d.popitem()
print("Popitem:", last_item)
print("After popitem:", d)

# fromkeys()
keys = ["a", "b", "c"]
new_dict = dict.fromkeys(keys, 0)
print("Fromkeys dict:", new_dict)

# clear()
d.clear()
print("After clear:", d)

# Built-in functions
print("Length of new_dict:", len(new_dict))
print("Type of new_dict:", type(new_dict))
