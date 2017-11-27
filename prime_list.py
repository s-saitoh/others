# coding: utf-8

prime_list = [2]

for x in range(3, 100, 2):
    a = False
    for y in prime_list:
        if y * y > x:
            a = True
            break
        if x % y == 0:
            break
    if a:
        prime_list.append(x)

print(prime_list)