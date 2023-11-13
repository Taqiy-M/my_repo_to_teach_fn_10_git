class Cart:
    def __init__(self, id, user, sana, holat):
        self.__id = id
        self.__user = user
        self.__sana = sana
        self.holat = holat
        self.__narx = 0
        self.__bonus = 0

    def get_narx(self):
        print(f"Narx:{self.__narx}\nBonus:{self.__bonus}")
        return self.__narx

    def set_narx(self, a):
        self.__narx += a-a/20
        self.__bonus += a/20



class Order:
    def __init__(self, product, amount, cart):
        self.product = product
        self.amount = amount
        self.cart = cart
        self.narx = product._narx * amount
        cart.set_narx(self.narx)
        product._user.set_daromad(self.narx)

