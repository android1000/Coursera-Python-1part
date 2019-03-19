obj = File("1.txt")
print(obj)
for line in obj:
    print(line)
obj.write("new_str")
print(obj)
for line in obj:
    print(line)
