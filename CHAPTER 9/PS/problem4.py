words = ["snake","animal"]

with open ("snake.txt" , "r") as  f:
    content = f.read()

for word in words:
    content = content.replace(word,"#"*len(word))

with open("snake.txt", "w") as f:
    f.write(content)