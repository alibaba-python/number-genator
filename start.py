a = 1
while True:
    size = input("enter a number(it will be 1 to your number):")
    size = int(size)
    size += 1
    while a < size:
        print(a)
        a += 1