"""
输入一个数，求质因数
"""
n = int(input())
i = 2
while i <= n:
    while n%i == 0:
        n /= i
        print(str(i),end=" ")
    i += 1