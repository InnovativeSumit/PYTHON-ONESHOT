# Open file in append mode
with open("files.txt", "a") as f:
    f.write("This line is appended.\n")  # \n for new line

# Verify by reading
with open("files.txt", "r") as f:
    print(f.read())
