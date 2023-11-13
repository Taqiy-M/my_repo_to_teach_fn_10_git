from abc import ABC, abstractmethod, abstractproperty


class Polygon(ABC):
    @abstractmethod
    def no_of_sides(self):
        pass

    @abstractmethod
    def hello(self):
        pass

    @abstractmethod
    def no_of_sides2(self):
        pass

    @abstractmethod
    def hello2(self):
        pass

    @abstractmethod
    def no_of_sides3(self):
        pass

    @abstractmethod
    def hello3(self):
        pass

    @abstractmethod
    def no_of_sides4(self):
        pass

    @abstractmethod
    def hello4(self):
        pass

    @abstractmethod
    def no_of_sides5(self):
        pass

    @abstractmethod
    def hello5(self):
        pass

    def salomaaat(self):
        pass


class Triangle(Polygon):

    def no_of_sides(self):
        pass

    def hello(self):
        pass

    def no_of_sides2(self):
        pass

    def hello2(self):
        pass

    def no_of_sides3(self):
        pass

    def hello3(self):
        pass

    def no_of_sides4(self):
        pass

    def hello4(self):
        pass

    def no_of_sides5(self):
        pass

    def hello5(self):
        pass




class Hero(ABC):
    @property
    @abstractmethod
    def hp(self):
        return 100


class Poseidon(Hero):
    _hp = 100

    @property
    def hp(self):
        return self._hp


    @hp.setter
    def hp(self, a):
        self._hp = a

# a = Poseidon()
# a.hp = 70
# print(a.hp)





















