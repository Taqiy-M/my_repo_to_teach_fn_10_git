class User:
    def __init__(self, fish, email, telefon, yil, jins, manzil):
        self.__manzil = manzil
        self.__jins = jins
        self.__yil = yil
        self.__telefon = telefon
        self.__email = email
        self.__fish = fish
        self.__daromad = 0


    def set_daromad(self, a):
        self.__daromad += a

    def get_daromad(self):
        return self.__daromad

    def get_manzil(self):
        return self.__manzil

    def get_jins(self):
        return self.__jins

    def get_email(self):
        return self.__email

    def get_telefon(self):
        return self.__telefon

    def get_fish(self):
        return self.__fish

    def get_yil(self):
        return self.__yil


