# try:
#     b = int(input())
#     a = int(input())
#     print(b/a)
# except ValueError:
#     print("Butun son kiriting?")
# except ZeroDivisionError:
#     print("Nolga bo'lish mumkin emas!!")









# input("n=")
# input()
# input()
#
# "12 45 89"


# a = int(input("n="))
# l = []
# for i in range(a):
#     l.append(list(map(int, input().split())))
#
# li = []
# d = 0
# d2 = 0
# for j in range(len(l)):
#     d2 += l[j][-1-j]
#     u = 0
#     q = 0
#     for i in range(len(l)):
#         u += l[i][j]
#         q += l[j][i]
#         if i == j:
#             d += l[i][j]
#     li.append(u)
#     li.append(q)
#
# li.append(d)
# li.append(d2)
# print(li)
#
# if li.count(li[0]) == len(li):
#     print("YES")
# else:
#     print("NO")

















# sonlar = [
#     (24, 50),
#     (400, 134),
#     (9, 819),
#     (50, 13),
#     (900, -129),
#     (10, 9)
# ]

# sonlar = sorted(sonlar, key=lambda x: x[1])
# print(sonlar)


# d = {
#     "a": 20, "ab": 10, "b": 90, "g": 40, "d": 15,
#     "h": 91, "j": -1, "t": 82, "y": 16, "u": 100, "q": 1
# }
#
# l = list(d.items())
#
# l = sorted(l, key=lambda u: u[1], reverse=True)
# print(l[:5])



# n = "45+32*(23+(23+x)*5)/(2+y)"
# b = set(list(n))
# print(n)
# l = {}
# for i in b:
#     if not i.isalnum():
#         l[i] = n.count(i)
# print(list(l.items()))


# d = dict()
# while True:
#     a = int(input("n="))
#     if a == -1:
#         break
#     try:
#         d[a] = d[a] + 1
#     except:
#         d[a] = 1
#
# print(d)



# n = input()
# d = {}
# for i in n:
#     if not i.isalnum():
#         try:
#             d[i] += 1
#         except:
#             d[i] = 1
#
# for k, v in d.items():
#     if k == ")":
#         continue
#     if k == '(':
#         print(f"() amali {v} ta", end=", ")
#         continue
#     print(f"{k} amali {v} ta", end=", ")
# print("ishlatilgan")


# b = input().split()
# l=[]
# for a in b:
#     l.append(a[-1] + a[1:-1] +a[0])
# print(l)



# a = input("Enter string: ").split()
# a[0] = a[0][::-1]
# a[-1] = a[-1][::-1]
# a = ["Salom", "alik", "Qales", 'ishlar', 'yaxshimu']
# a[0] = a[0][::-1]
# a[-1] = a[-1][::-1]
# for i in a:
#     print(i, end=" ")




# l = [2, 2, 6, 7, 6, 7, 9, 0, 9, 1, 0]

a = ["Imomali", "yusuf", "taqiy",
     "Kamron", "zohid", "abdul", "ali", "Alyor",
     "Kamola","Mushtariy", "Malika"]


import random
random.shuffle(a)
random.shuffle(a)

print(a[:5])
print(a[5:])
