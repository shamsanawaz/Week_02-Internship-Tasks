try:
    file = open("date.txt", "r")
    content = file.read()
    print(content)
    file.close()
except FileNotFoundError:
    print("Error: File not found .Please check the file name.")