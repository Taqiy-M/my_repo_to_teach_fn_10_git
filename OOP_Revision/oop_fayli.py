from abc import ABC, abstractmethod


class ShipBlueprint(ABC):
    @abstractmethod
    def tezlashish(self):
        pass

    def yelkanlarni_kotarish(self):
        pass

    @abstractmethod
    def burilish(self):
        pass

    @abstractmethod
    def langar_tashlash(self):
        pass

    @abstractmethod
    def tor_tashlash(self):
        pass

    @abstractmethod
    def danger(self):
        pass




class Ship(ShipBlueprint):
    def tezlashish(self, a=10):
        pass

    def burilish(self, a=5):
        pass

    def langar_tashlash(self):
        pass

    def tor_tashlash(self):
        pass

    def danger(self):
        pass

    def __init__(self, nom, brend, sigim, max_tezlik, narx):
        self.__nom = nom
        self.__narx = narx
        self.__max_tezlik = max_tezlik
        self.__sigim = sigim
        self.__brend = brend
        self.__tezlik = 0
        self.__langar_pastda = True
        self.__yeklan = False
        self.__sos = "SOS SOS SOS YORDAM PLIZ"













