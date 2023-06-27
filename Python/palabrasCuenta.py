a = input("Ingrese una palabra: ")
count = 0
b = 0
for b in a:
    if (b == "a" or b == "A"):
        count = count + 1
print(count)