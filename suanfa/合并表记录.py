count = input()
numbers = []
i = 0
while i < int(count):
    a,b = input().split()
    numbers.append([int(a),int(b)])
    i += 1
# numbers = numbers.sort()
print(sorted(numbers))