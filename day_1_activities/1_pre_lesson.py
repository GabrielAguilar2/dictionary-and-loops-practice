# this is what we will use for the video intro to dictionaries

# dictionary = a collection of {key:value} pairs ordered and changeable. No duplicates.
capitals = {"USA": "Washington D.C.", "India": "New Delhi", "China": "Beijing", "Russia": "Moscow"}

print(dir(capitals))
print(help(capitals))
print(capitals.get("Japan"))

if capitals.get("Japan"):
    print("That capitol exists")
else:
    print("That capitol doesn't exist")




keys = capitals.keys()

for key in capitals.key():
    print(key)

values = capitals.values()
for value in capitals.values():
    print(value)

items = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")


