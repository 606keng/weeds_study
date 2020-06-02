def word1(word):
    num = len(word)
    if word.strip() == "" or num == 8:
        print(word)
    elif num < 8:
        print(word+(8-num)*"0")
    else:
        n = int(num/8)
        m = num%8
        for i in range(n):
            print(word[i*8:(i+1)*8])
        print(word[n*8:num] + (8-m)*"0")
a=input()
b=input()
word1(a)
word1(b)