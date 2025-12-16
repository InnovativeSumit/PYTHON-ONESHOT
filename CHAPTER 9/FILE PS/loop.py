with open("files.txt", "r") as f:
    for line in f:
        print(line, end="")  # end="" prevents extra blank lines
