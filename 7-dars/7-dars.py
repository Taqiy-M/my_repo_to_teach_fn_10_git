
import math


# math.pow(3, 2)
# print(int(math.sqrt(400)))
# print(math.log(100, 10))

# a = math.degrees(1)
# print(2*math.pi*a)
# a = math.radians(90)
# print(math.sin(a))
# a = math.ceil(4.001)
# print(round(4.51))

import random as r


# print(random.uniform(10, 50))
# print(r.randrange(0, 1000, 3))


l = ["Abdusattor", "Murodali",
     "Muhammadiyor", "Samandar R",
     "Samandar T", "Ozodbek",
     "Azizbek", "Behruz", "Doston", "Shohruh"]

# print(r.choice(l))
# print(l)
# r.shuffle(l)
# print(l)
# r.shuffle(l)
# print(l)

l = list()
for i in range(50):
    l.append(r.randint(0, 100))
# print(l)
#
# input()
# print(r.choice(l))
# print(r.choice(l))
# print(r.choice(l))
# print(r.sample(l, 4))


# import sys
# print(sys.setrecursionlimit(10000))
# print(sys.getrecursionlimit())

import os

# salom nomli papkani o'chirib yuborish
# os.rmdir("salom")

# hozirgi turgan path ni olish
# print(os.getcwd())

# biz turgan papkadagi fayl va papkalar ro'yxati
# print(os.listdir())

# 7-dars nomli papkaga kirish
# os.chdir("7-dars")
# print(os.listdir())

# 3 ta papka ortga qaytish
# os.chdir("../../..")
# print(os.getcwd())

# papka yaratish
# os.mkdir("dars")
# os.mkdir("dars1")
# os.mkdir("dars2")
# os.rename("papka1", "dars1")
# for i in range(13, 30):
    # os.rmdir(f"Dars{i}")
    # os.rename(f"Dars{i}", f"Papka{i}")
    # os.mkdir(f"Dars{i}")
# os.removedirs("Olimjon.py")
# from colorama import Fore, Back, init, Style
# init()
# print(Fore.WHITE+Back.LIGHTRED_EX+"Assalomu alaykum!!")
# print("Hello World!")
# print(Style.RESET_ALL)
# print("Salomat bo'ling!!")

d = {
    "ism": "Ali",
     "yosh": 17
}
#
# l = [132, 54, 234, 76,345, 0]
# print(l[6])
# a = input("a=")
# b = input("b=")
# c = 0
# try:
#     a = int(a)
#     b = int(b)
#     c = a/b
#     print(d['nom'])
#     print(f"Bo'linma: {c}")
#
# except ValueError:
#     print("Butun son kiriting!!!")
# except ZeroDivisionError:
#     print("Nolga bo'lish mumkin emas!!!")
# except Exception as e:
#     print(f"Qandaydir xatolik yuz berdi!!{type(e).__name__}")
# finally:
#     print("Xayr!!!!")



i = int(input("Faqat manfiy son kirit: "))

if i >= 0:
    raise ZeroDivisionError("FAQAT MANFIY SON KIRITISH KERAK EDI!!")






























