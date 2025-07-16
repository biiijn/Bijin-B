a = int(input("Enter a: "))
i = 0
num = 1

while i < a:
    print(num, end=", " if i < a - 1 else "")
    num += 2
    i += 1
