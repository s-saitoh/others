def quick_sort(buffer, low, high):
    # python3は/だと小数点以下も表示されるので、TypeErrorになる、//を使え
    pivot = buffer[(low + high)//2]
    i = low
    j = high
    while True:
        while pivot > buffer[i]:
            i += 1
        while pivot < buffer[j]:
            j -= 1
        if i >= j:
            break
        tmp = buffer[i]
        buffer[i] = buffer[j]
        buffer[j] = tmp
        i += 1
        j -= 1
    if low < i - 1:
        quick_sort(buffer, low, i - 1)
    if high > j + 1:
        quick_sort(buffer, j + 1, high)

a = [5, 9, 1, 8, 2, 7, 3, 6, 4]
quick_sort(a, 0, 8)
print(a)