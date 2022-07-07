from abc import ABC, abstractmethod


class Fabric(ABC):

    def __init__(self, param):
        self.param = param

    @abstractmethod
    def my_def(self):
        pass

    def __str__(self):
        return str(self.param)


class Coat(Fabric):

    @property
    def my_def(self):
        return self.param / 6.5 + 0.5 + 1
# где 1 - запас


class Suit(Fabric):
    @property
    def my_def(self):
        return self.param * 2 + 0.3 + 1


clothes_1 = Coat(52)
clothes_2 = Suit(176)
print(clothes_1)
print(clothes_2)
print(clothes_1.my_def)
print(clothes_2.my_def)
