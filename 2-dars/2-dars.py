# class Car:
#     def __init__(self, nom, brend, narx, maks_tezlik):
#         self.started = False
#         self.tezlik = 0
#         self.nom = nom
#         self.brend = brend
#         self.narx = narx
#         self.maks_tezlik = maks_tezlik
#
#     def start(self):
#         if not self.started:
#             print(f"{self.nom} mashina yondi.")
#             self.started = True
#         else:
#             print("Kalitti burormen, sindirvorasiz")
#
#
#     def stop(self):
#         pass
#
#     def tezlash(self, a=5):
#         if not self.started:
#             print("Avval kalitni burang!")
#             return
#         if self.tezlik+a <= self.maks_tezlik:
#             self.tezlik += a
#         else:
#             self.tezlik = self.maks_tezlik
#         print(f"Hozirgi tezlik {self.tezlik}")
#
#     def sekinlash(self):
#         pass
#
# a = Car("Nexia-3", "Chevrolet", 1000, 220)
# b = Car("Tracker", "Chevrolet", 10000, 300)
#
#
# a.start()
# b.start()
# b.tezlash(200)
# b.tezlash(200)
# b.tezlash()
# b.tezlash()
# b.tezlash()
# b.tezlash()
# b.tezlash()



# parent class
# child class



class Animal:
    def __init__(self, name, year, tirik, vazn):
        self.name = name
        self.year = year
        self.tirik = tirik
        self.vazn = vazn

    def taom(self):
        print("Taomlanish.. Xam xam")

    def ovoz(self):
        raise NotImplementedError("Ovoz methodini yaratmadingiz.")

    def show(self):
        print(f"Otim {self.name}")
        print(f"Yoshim {2023-self.year}")
        print(f"{self.vazn} kiloman")



class Cat(Animal):
    def __init__(self, name, year, tirik, vazn):
        super().__init__(name, year, tirik, vazn)

    def ovoz(self):
        print("Myau myau mau")
        print("Myau myau mau")


class Dog(Animal):
    def __init__(self, name, year, tirik, vazn):
        super().__init__(name, year, tirik, vazn)

    def ovoz(self):
        print("Vov vov vov")
        print("Vov vov vov")


# a = Cat("Baroqvoy", 2022, True, 3.5)
# b = Dog("Olapar", 2021, True, 10)
# a.ovoz()


# polymorfizm

# method overloading

# a = "Hello"
# b = ["hello", "world"]
# c = ("hello", "world")
# d = {
#     "ism": "Ahmad",
#     "yosh": 25,
#     "univer": "INHA"
# }
# e = {13, 245, 54, 1245, 654, 23, 12, 245, 54, 654, 23}
# print(len(e))



# operator overloading
# operator unga berilayotgan operandlarga asoslanib
# har safar har xil ishlayapti
# print(1 + 2)
# print("1"+"2")
# print("25"*10)
# print(25*10)



# method overriding
# ota klassdan olingan metodni bola klasda qaytadan yozish overriding bo'ladi



# duck typing

class Uzbek:
    def hello(self):
        print("Assalomu alaykum!!")

class English:
    def hello(self):
        print("Hello")

class Chinese:
    def hello(self):
        print("Nihao")

class Korean:
    def hello(self):
        print("Annyohaseyo")



def intro(a):
    a.hello()


# a = Chinese()
# b = English()
# intro(b)


class Talaba:
    def __init__(self, ism, guruh, gpa, kurs, yosh):
        self.ism = ism
        self.guruh = guruh
        self.gpa = gpa
        self.kurs = kurs
        self.yosh = yosh

    def __str__(self):
        return f"{self.ism} {self.guruh}"

    def __repr__(self):
        return f"{self.ism}"

    def __eq__(self, other):
        return self.yosh == other.yosh

    def __gt__(self, other):
        return self.yosh > other.yosh

    def __ge__(self, other):
        return self.yosh >= other.yosh

    def __add__(self, other):
        if isinstance(other, int):
            self.yosh += other
        if isinstance(other, Talaba):
            self.yosh += other.yosh
        return self.yosh








a = Talaba("Abdurahmon", "Blue", 3.8, 3, 23)
b = Talaba("Abduvali", "Green", 2.95, 2, 30)
c = Talaba("Ali", "Blue", 3.8, 3, 21)
d = Talaba("Zohid", "Green", 2.95, 2, 40)
e = Talaba("Azizbek", "Blue", 3.8, 3, 44)
f = Talaba("Ahadjon", "Green", 2.95, 2, 19)
g = Talaba("Rasul", "Blue", 3.8, 3, 32)


# print(g+1)
# print(g.yosh)
# l = [a, b, c, d, e, f, g]
# print(l)
# l.sort()
# print(l)






# print(a)
# l = [a, b, b, a, b, b, a]
# print(l)







class Shape:
    nom = ""
    def area(self):
        raise NotImplementedError("Yuza hisoblash "
                                  "metodi kiritilmagan")
    def perim(self):
        raise NotImplementedError("Perimetr hisoblash "
                                  "metodi kiritilmagan")

class Circle(Shape):
    radius = 0
    def area(self):
        pass
    def perim(self):
        pass

class Rect(Shape):
    a, b = 0, 0
    def area(self):
        pass
    def perim(self):
        pass

class Tri(Shape):
    a, b, c = 0, 0, 0

    def perim(self):
        pass



# class Inson:
#     name = ""
#     age = 0


# class Student(Inson):
    # univer = ""
    # kurs = 0
    # baho = 0







