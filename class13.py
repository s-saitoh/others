# コンポジション
# 継承よりもコンポジションや集約の方が理に適っている場合がある

class Bill():
    def __init__(self, description):
        self.description = description

class Tail():
    def __init__(self, length):
        self.length = length

class Duck():
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail
    def about(self):
        print('This duck has a', self.bill.description, 'bill and a', self.tail.length, 'tail')

# bill, tailオブジェクトを作り、あたらしいduckオブジェクトに与える
tail = Tail('long')
bill = Bill('wide orange')
duck = Duck(bill, tail)
duck.about()