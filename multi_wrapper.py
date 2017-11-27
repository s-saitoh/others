# 並列計算を使えるように
from multiprocessing import Pool

# aとbをかけ算するだけの関数
def kakezan(a, b):
    return a * b


# ラッパー
def wrapper_kakezan(args):
    return kakezan(*args)

# 並列計算実行
if __name__ == '__main__':
    tutumimono = [[i, 3] for i in range(10)]
    p = Pool(processes=2)
    print(p.map(wrapper_kakezan, tutumimono))