# a = [1,3,2]
#
# a.reverse()
# print(a)
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)
# a = [0,0,0]
# if sum(a):
#     print(123)

from curses.ascii import isalnum

a="asdfsdf123  ,.,.,.,.3123"
a = list(filter(isalnum,a))
print(a)