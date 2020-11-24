"""
给定一个列表，求出全排列
"""
def permutations(alist: list) -> list:
    '''这是一个枚举排列的函数

    :参数 alist:一个包含不重复元素的列表
    '''
    # 基线条件是列表里只有一个元素，直接返回
    if len(alist) == 1:
        return str(alist[0])
    # 求出元素的个数
    n = len(alist)
    # 这是用于存储所有排列的列表
    ans = []
    # 遍历这些元素，依次让这些元素做排头兵
    for i in range(n):
        # 调用递归函数，对除了排头兵以外的剩下的元素进行排列
        # 对得到的每种排列，都把排头兵拼在最前面，得到全部元素的排列，添加到答案列表里
        for each in permutations(alist[0:i] + alist[i + 1:n]):
            ans.append(str(alist[i])+ str(each))
    # 返回答案
    return ans
a = [1,2,3]
print(permutations(a))