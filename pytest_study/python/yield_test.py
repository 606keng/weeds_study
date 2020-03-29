def a():
    for i in range(10):
        print("setup")
        yield i
        print("teardown")

for b in a():
    print(b )