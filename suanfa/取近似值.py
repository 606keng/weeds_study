a = str(input()).split(".")
if int(a[1][0]) < 5:
    print(int(a[0]))
else:
    print(int(a[0]) + 1)