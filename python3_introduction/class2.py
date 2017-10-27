# プロパティによる属性値の取得、設定
# 非公開にしておきたい属性の値を読み書きする
class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    def get_name(self):
        print('inside the getter.')
        return self.hidden_name
    def set_name(self, input_name):
        print('inside the setter.')
        self.hidden_name = input_name
    name = property(get_name, set_name)  # この行により、nameを参照すると実際にはget_name()が参照される


fowl = Duck('Howard')
print(fowl.name)

# get_name()を直接呼び出す
fowl.get_name()

# nameに名前を挿入するとset_nameメソッドが呼び出される
fowl.name = 'Daffy'
print(fowl.name)

# set_nameを直接呼び出す
fowl.set_name('Daffy')
print(fowl.name)