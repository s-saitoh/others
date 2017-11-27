class Bar(Foo): # Fooクラスを継承
    def __init__(self, x, y, z):
        Foo.__init__(self, x, y)
        self.c = z


    def get_c(self):
        return self.c