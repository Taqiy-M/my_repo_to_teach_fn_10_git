

# fayl = open("Tillayev.txt", "x")
# fayl.close()

# fayl = open("Behruz.txt", 'w')
# fayl.write("Assalomu alaykum Behzod!\n")
# fayl.close()

# my_l = []
# while True:
#     a = input("Ism kiriting: ")
#     if a.lower() == "stop":
#         break
#     my_l.append(a+"\n")

# with open("Muhammaddiyor.txt", "w") as qovun:
#     qovun.write("Salom Dunyo!!\nMen tug'ildim!!\n")
#     qovun.writelines(my_l)

# with open("Olimjon.txt", "w") as o:
#     o.writelines(my_l)
#     print(f"Hozir turgan joy: {o.tell()}")
#     o.seek(0)
#     print(f"Hozir turgan joy: {o.tell()}")
#     o.write("Salomat bo'lasizzz!!!!")


# import random
# l = list()
# for i in range(1000):
#     a = random.randint(0, 1000)
#     l.append(a)

# l = list(map(lambda x: str(x)+"\n", l))
# with open("sonlar.txt", "w") as s:
#     s.writelines(l)

# with open("Doston.txt", "w") as monti:
#     monti.write("Salom! Nima gap!\n")


# with open("Olimjon1.txt", "w+") as qovun:
    # qovun.readline()
    # qovun.readline()
    # qovun.readline()
    # a = qovun.read()
    # a = qovun.readlines()
    # a = qovun.readline()

# print(a)

import random
import pickle

# with open("Ozod.bin", "rb") as faylim:
#     for i in range(10):
#         a = pickle.load(faylim)
#         print(a)

# with open("Ozod.bin", "ab") as fayl:
#     for i in range(100):
#         a = random.randint(0, 1000)
#         pickle.dump(a, fayl)

# with open("ozodbek.pkl", "ab") as faylim:
#     pickle.dump(200, faylim)
    # a = pickle.load(faylim)

# with open("ozodbek.pkl", "rb") as fayl:
#     while True:
#         try:
#             print(pickle.load(fayl))
#         except:
#             print("Fayl Oxiriga yetdi")
#             break


#     a = pickle.load(fayl)
#     b = pickle.load(fayl)
# print(a)
# print(b)


# from openpyxl import Workbook, load_workbook

# fayl = Workbook()
# fayl = load_workbook("otchot.xlsx")
# sh = fayl.active

# sh["A1"] = "ID"
# sh["B1"] = "ISM"
# sh["C1"] = "YOSH"
# a = 5
# while True:
#     a += 1
#     b = input("Ism kirit: ")
#     if b.lower() == "stop":
#         break
#     c = int(input("Yosh kirit: "))
#     sh[f"A{a}"] = a - 1
#     sh[f"B{a}"] = b
#     sh[f"C{a}"] = c
# fayl.save("otchot.xlsx")






























































