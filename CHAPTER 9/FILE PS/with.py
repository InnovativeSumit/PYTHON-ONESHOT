with open("files.txt", "w") as f: # w mean write 
    f.write("Hello, this file is created by Python")

with open("files.txt", "r") as f: # r is read
    print(f.read())
