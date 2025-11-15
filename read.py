f = open ("sample.txt", "r")
data = f.read()
print(data)
f.close()

f = open("sample.txt", "w")
f.write("Hello Python!")
f.close()


f = open("sample.txt", "a")
f.write("\nNew line added.")
f.close()
