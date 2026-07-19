# file = open("classified.txt")

# content = file.readlines()
# print(content)

# for line in file:
#     print(line.strip())

# file.close()

with open("classified.txt", "r") as file:
    data = file.read()

print(data)