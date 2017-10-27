n = 42
f = 7.03
s = 'string cheese'

# 古い書き方
print('%d %f, %s' % (n, f, s))

print('%d %f, %.2s' % (n, f, s))

# 新しい書き方、引数指定
print('{} {} {}'.format(n, f, s))

print('{2} {0} {1}'.format(n, f, s))

