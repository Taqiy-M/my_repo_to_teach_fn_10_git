class Product:
    def __init__(self, nom, narx, sana, user):
        self._nom = nom
        self._narx = narx
        self._sana = sana
        self._user = user


class Cloth(Product):
    def __init__(self, nom, narx, sana, user, brend, size, rang):
        super().__init__(nom, narx, sana, user)
        self._brend = brend
        self._size = size
        self._rang = rang


class Gadget(Product):
    def __init__(self, model, narx, sana, user, brend, tur, holat):
        super().__init__(model, narx, sana, user)
        self.brend = brend
        self.tur = tur
        self.holat = holat

