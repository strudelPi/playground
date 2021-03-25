class Foo(object):
    def __init__(self, val):
        self._x = val

    @property
    def x(self):
        """hehe"""
        return self._x

    # @x.setter
    # def x(self, val):
    #     self._x = val

    @x.deleter
    def x(self):
        del self._x


a = Foo(4)

print(a.x)

a.x = 2

del a.x

