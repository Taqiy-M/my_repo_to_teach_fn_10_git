# constructor, destructor

# class Inson:
#     def __init__(self, ism, yil, kasb, jins):
#         self.ism = ism
#         self.yil = yil
#         self.kasb = kasb
#         self.jins = jins
#         print(f"Ismim {self.ism}")
#         print("Men tug'ildim!!!")
#
#     def ovqatlanish(self):
#         print("Bismillah....")
#         print("Mmmm... Ham ham...")
#         print("Xudoga shukr...")
#
#     def tanishish(self):
#         print(f"Mening ismim {self.ism}")
#         print(f"Mening yoshim {2023-self.yil}")
#         print(f"Mening kasbim {self.kasb}")


# bu joyda a, b, c == obyekt (object so'ziga instance so'zi sinonim)
# Inson esa klassdir!

# a = Inson("Jamshid", 1997, "Neyroxirurg", "Erkak")
# b = Inson("Ahmad", 2001, "Dasturchi", "Erkak")
# c = Inson("Shahrizoda", 1530, "Ertakchi", "Ayol")
# c.tanishish()

# b = Inson()
# a.ism = "Ahmad"
# a.yil = 2001
# a.kasb = "Dasturchi"
# a.jins = "Erkak"
# b.ism = "Jamshid"
# b.yil = 1999
# b.kasb = "Shifokor"
# b.jins = "Erkak"
# a.tanishish(1 ,2)
# print()
# b.tanishish()
# b = Inson()
# c = Inson()
# a.ism = "Abduvali"
# c.ism = "Alisher"
# print("A ning ismi: ", a.ism)
# print("C ning ismi: ", c.ism)


# class Talaba:
#     def __init__(self, ism, univer, year, gpa):
#         self.name = ism
#         self.univer = univer
#         self.year = year
#         self.gpa = gpa
#         print("Men tug'ildim!")

    # def show(self):
    #     print(f"Ismim {self.name}")
    #     print(f"{self.univer} ga {self.year} yili kirganman shetta o'qiyman")
    #     print(f"gpa bahoim {self.gpa}")

    # def nolish(self):
    #     print(f"Ismim {self.name}")
    #     print(f"{self.univer} ga {self.year} yili kirganman shetta o'qiyman. Kontraktla qimmat. Oson bo'mayapti")
    #     print(f"gpa bahoim {self.gpa}. O'zi atelab paslatvorishadi.")
    #     print("Dollarni kotarilishini qaren qiyinlashib ketyapti yashasham")


# a = Talaba("Ahmadali", "INHA", 2017, 4.1)
# b = Talaba("Jamshid", "ToshMI", 2018, 3.2)
# b.nolish()



import turtle
import _thread




class Chizma:
    def __init__(self, size, color, speed, shape, x, y):
        self.qalam = turtle.Turtle()

        self.qalam.up()
        self.qalam.pensize(size)
        self.qalam.color(color)
        self.qalam.speed(speed)
        self.qalam.shape(shape)
        # for i in range(20):
        #     self.qalam.right(90)
        self.qalam.goto(x, y)
        self.qalam.down()


    def sq(self, a):
        for i in range(4):
            self.qalam.fd(a)
            self.qalam.right(90)

    def ay(self, r):
        self.qalam.circle(r)


a = Chizma(10, "blue", 2, "classic", -300, 300)
b = Chizma(15, "red", 2, "turtle", 300, -300)
c = Chizma(10, "blue", 2, "classic", 300, 300)
d = Chizma(15, "red", 2, "turtle", -300, -300)


_thread.start_new_thread(a.sq, (100,))
_thread.start_new_thread(b.sq, (50,))
_thread.start_new_thread(c.sq, (50,))
_thread.start_new_thread(d.sq, (100,))




turtle.done()


class Hisob:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def qosh(self):
        pass

    def ayir(self):
        pass

    def kop(self):
        pass

    def gacha_kop(self):
        pass

    def summa(self):
        pass

    def qoldiq(self):
        pass

    def daraja(self):
        pass




h1 = Hisob(20, 468)
h2 = Hisob(90, 879)



h1.daraja()












