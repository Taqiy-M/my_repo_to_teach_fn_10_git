# operator overloading
# method overloading
# method overriding
# duck typing


class Inson:
    age = 0
    name = ""

    def salom(self):
        print("Assalomu alaykum. Men odamman!")


class Talaba(Inson):
    def salom(self):
        print("Assalomu alaykum! Men talabaman!")

    def hh(self):
        super().salom()

# a = Talaba()
# a.salom()
# print(isinstance(a, Inson))
# print(type(a))




class Human:
    def __init__(self):
        self._name = "Ali"

    def hello(self):
        print(f"Salom, mening ismim {self._name}")


class Student(Human):
    def __init__(self):
        super().__init__()

    def hello(self):
        print(f"Salom, mening ismim {self._name}")


class Ishchi(Student):
    def __init__(self):
        super().__init__()

    def hello(self):
        print(f"Salom, mening ismim {self._name}")

# a = Ishchi()
# print(a._name)






class Car:
    def __init__(self, nom, rang, narx, max_tezlik):
        self.nom = nom
        self.rang = rang
        self.narx = narx
        self.max_tezlik = max_tezlik
        self.__started = False
        self.__tezlik = 0


    def start(self):
        if not self.__started:
            print("Mashina ishga tushdi")
            self.__started = True
        else:
            print("Kalitti burormen. Mashina yoniq")


    def get_tezlik(self):
        return self.__tezlik


    def tezlashish(self, a=10):
        if not self.__started:
            return

        if self.__tezlik + a < self.max_tezlik:
            self.__tezlik += a
        else:
            self.__tezlik = self.max_tezlik


# a = Car("Matiz", "Sariq", 3500, 180)
# b = Car("Tracker", "Qora", 7000, 260)
# a.start()
# print("Hozirgi tezlik ", a.__tezlik)


# getter
# setter






class Airline:
    def __init__(self, nom, aeroport_soni, samolyot_soni):
        self.nom = nom
        self.aeroport_soni = aeroport_soni
        self.samolyot_soni = samolyot_soni


class Flight:
    def __init__(self, nom, sigim, yonalish, u_vaqt, q_vaqt, airl):
        self.q_vaqt = q_vaqt
        self.u_vaqt = u_vaqt
        self.yonalish = yonalish
        self.sigim = sigim
        self.nom = nom
        self.airl = airl
        self.seats = []
        for i in range(0, sigim):
            self.seats.append(i)



class Passenger:
    def __init__(self, fish, yosh, passport, address):
        self.__fish = fish
        self.__yosh = yosh
        self.__passport = passport
        self.__address = address

    def get_fish(self):
        return self.__fish

    def get_yosh(self):
        return self.__yosh

    def get_passport(self):
        return self.__passport

class Booking:
    def __init__(self, passengers, flight, zakaz_vaqti):
        self.passengers = passengers
        self.flight = flight
        self.zakaz_vaqti = zakaz_vaqti
        self.price = 250*len(passengers)





a = Airline("O'zbekiston Havo Yo'llari MCHJ", 8, 95)
b = Flight("3445A", 200, "Toshkent - NewYork", "08:00", "21:05", a)
c = Flight("3115B", 320, "Toshkent - Jidda", "11:20", "15:30", a)
d = Flight("9406A", 300, "Farg'ona - Riyod", "08:00", "21:05", a)

aa = Passenger("Abduvali Jonbekov", 35, "AA1109080", "Andijon")
ab = Passenger("Abdushukur Jonbekov", 40, "AA1009180", "Andijon")
ac = Passenger("Xosiyatxon Jonbekova", 31, "BA1820131", "Andijon")
ad = Passenger("Hadichaxon Jonbekova", 35, "AB1109170", "Andijon")
ae = Passenger("Hadichaxon Jonbekova", 35, "AB1109170", "Andijon")

bb = Booking((aa, ab, ac, ad, ae), c, "20:08")


