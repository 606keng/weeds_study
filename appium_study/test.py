a = [1,2,3]
b = a[:]
for i in range(len(a)):
    if b:
        print(a[i])
        b.pop(0)
        print(b)
