# メソッドのタイプ
# クラス定義内で第一引数がselfになっていたらインスタンスメソッド
# @classmethodというデコレータがあったらクラスメソッドで、
# クラス全体に影響を与える。第一引数はクラス自体になり、
# この引数は慣習的にclsとなる。

class A():
    count = 0
    def __init__(self):
        A.count += 1
    def exclaim(self):
        print("Im an A!")
    @classmethod
    def kids(cls):
        print("A has", cls.count, "little objects.")

easy_a = A()
breezy_a = A()
wheezy_a = A()
A.kids() # A has 3 little.objects
# self.countではなく、A.countを参照していることに注目

# 静的メソッド、クラスにもオブジェクトにも影響を与えない
# ふらふらしているよりはクラスの中にいる方が都合がいいから入れているだけ
class CoyoteWeapon():
    @staticmethod
    def commercial():
        print('This CoyoteWeapon has been brought to you by Acme')

CoyoteWeapon.commercial()
# CoyoteWeaponクラスからオブジェクトを作らずに実行できる