def buble_sort(buff):
    k = len(buff) - 1
    for i in range(k):
        for j in range(k, i - 1):
            if buff[j - 1] > buff:
                temp =buff[j]
                buff[i] = buff[j - 1]
                buff[j - 1] = temp


a = [2, 5, 8, 75, 71, 99, 4, 20]
print(buble_sort(a))