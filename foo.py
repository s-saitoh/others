class Foo:
    def __init__(self, x, y):
        self.a = x
        self.b = y


    def get_a(self):
        return self.a


    def get_b(self):
        return self.b


class Bar(Foo): # Fooクラスを継承
    def __init__(self, x, y, z):
        Foo.__init__(self, x, y)
        self.c = z


    def get_c(self):
        return self.c


    print(str(get_c))