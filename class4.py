class Circle():
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2 * self.radius

c = Circle(5)

print(c.radius)
print(c.diameter)

c.radius = 7
print(c.diameter)

#c.diameter = 20 # cannot set attribute

# 読み出し専用のプロパティを作るときに便利
# プロパティの属性を書き換えても、クラス定義内のコードを書き換えるだけですみ
# 呼び出し元には手を付けずにすむのがメリット