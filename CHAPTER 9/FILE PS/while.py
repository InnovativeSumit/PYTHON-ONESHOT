with open("files.txt", "r") as f:
    line = f.readline()  # read the first line
    while line:
        print(line, end="")  # print the line without adding extra newline
        line = f.readline()  # read the next line
