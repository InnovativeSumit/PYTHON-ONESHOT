# Create a set
s = {1, 2, 3, 4, 5, 5}   # duplicates removed automatically

print("Original set:", s)
print("Type:", type(s))
print("Length:", len(s))
print()

# add()
s.add(6)
print("After add:", s)

# update()
s.update([7, 8], {9, 10})
print("After update:", s)

# remove()
s.remove(2)
print("After remove:", s)

# discard()
s.discard(100)   # no error if element not present
print("After discard:", s)

# pop()
removed = s.pop()
print("Popped element:", removed)
print("After pop:", s)

# copy()
s_copy = s.copy()
print("Copy of set:", s_copy)

# union()
s2 = {5, 6, 11}
print("Union:", s.union(s2))

# intersection()
print("Intersection:", s.intersection(s2))

# difference()
print("Difference:", s.difference(s2))

# symmetric_difference()
print("Symmetric Difference:", s.symmetric_difference(s2))

# issubset()
print("Is subset:", {5, 6}.issubset(s.union(s2)))

# issuperset()
print("Is superset:", s.union(s2).issuperset({5, 6}))

# isdisjoint()
print("Is disjoint:", {100, 200}.isdisjoint(s))

# clear()
s.clear()
print("After clear:", s)

# empty set
empty_set = set()
print("Empty set:", empty_set)
print("Type of empty set:", type(empty_set))
