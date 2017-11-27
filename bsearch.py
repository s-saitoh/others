# 二分探索
def bsearch(x, ls):
    low = 0
    high = len(ls) - 1
    while low <= high:
        middle = (low + high) // 2

        if x == ls[middle]:
            return True
        elif x > ls[middle]:
            low = middle + 1
        else:
            high = middle -1
    return False


a = [11, 22, 33, 44, 55, 66, 77, 88, 99]
print(bsearch(44, a))
print(bsearch(40, a))