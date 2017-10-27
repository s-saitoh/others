
class Person():
    def __init__(self, name):
        self.name = name

"""
hunter = Person('Elmer Fudd')
print(hunter.name)
"""
# 継承
class Car():
    def exclaim(self):
        print("Im a car!")

class Yugo(Car): # Carクラスを継承
    def exclaim(self):
        print("Im a Yugo! Much like a Car, but more Yugo-ish.")
    def need_a_push(self):
        print("A little help here?")


give_me_a_car = Car()
give_me_a_Yugo = Yugo()

give_me_a_car.exclaim()
give_me_a_Yugo.exclaim()

# メソッドのオーバーライド
class MDPerson(Person): #Personクラスを継承
    def __init__(self, name):
        self.name = " Doctor " + name

class JDPerson(Person): #Personクラスを継承
    def __init__(self, name):
        self.name = name + ", Esquire."

person = Person("Fudd")
doctor = MDPerson("Fudd")
lawyer = JDPerson("Fudd")

print(person.name)
print(doctor.name)
print(lawyer.name)

# 子クラスだけメソッドの追加
give_me_a_Yugo.need_a_push()

# superによる親への支援要請
"""
super()が親クラスのPersonの定義を取り出す
Person()が受け付けるオプション引数はnameだけ
super()を使うメリット……Person()が変更になったとき、EmailPersonも連動して変更されるので、
わざわざ書き換える必要がなくなり、バグを減らせる
"""
class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email

bob = EmailPerson('Bob Frapples', 'bob@frapples.com')
print(bob.name)
print(bob.email)



