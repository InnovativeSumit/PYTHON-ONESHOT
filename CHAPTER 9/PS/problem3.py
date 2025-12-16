word = "snake"

with open ("snake.txt" , "r") as  f:
    content = f.read()

contentnew = content.replace(word,"#####")

with open("snake.txt", "w") as f:
    f.write(contentnew)