# E-commerce Platform:
# Create a sophisticated e-commerce platform
# with classes for User, Product, ShoppingCart, and Order.
# Users can be both customers and sellers.
# Implement an intricate order processing system,
# with multiple payment methods and shipping options.
# Apply encapsulation to secure user
# and payment information.
# Demonstrate polymorphism by processing
# orders from different types of users.
from orders import Order, Cart
from products import Cloth, Gadget
from users import User


u = User("Abduvali Rajabov", "abdushka@sfak.com",
         "99 999 88 78", 1984, "M",
         "Qo'qon shahar, Marifat 28")
u1 = User("Abdushukur Holmatov", "hheehee@sfak.com",
         "91 988 09 78", 1981, "M",
         "Andijon shahar, Shaytanat 128")
u2 = User("Toshtemir Toshov", "stone@sfak.com",
         "91 008 09 07", 2001, "M",
         "Toshkent, Toshko'mirchi 101")


p1 = Cloth("T-shirt 99", 23, "09.09.2023", u2, "Tommy Hilfiger", "L", "white")
p2 = Cloth("Jacket 101", 320, "09.09.2023", u2, "Tommy Hilfiger", "XL", "black", )
p3 = Cloth("Trousers ff4", 132, "09.09.2023", u2,  "Fashion", "M", "khaki")
p4 = Cloth("T-shirt ", 48, "09.09.2023", u2,  "Levi's", "XL", "cyan")
p5 = Gadget("iPhone 13 pro Max", 1200, "09.09.2022", u2, "Apple", "smartphone", "new")
p6 = Gadget("Galaxy S23 pro Max", 1100, "08.09.2022", u2, "Samsung", "smartphone", "new")


c1 = Cart(1, u, "10.10.2023", "pending")
c2 = Cart(2, u1, "10.11.2023", "pending")


o1 = Order(p1, 4, c1)
o2 = Order(p4, 2, c1)
o3 = Order(p6, 1, c1)
o4 = Order(p5, 2, c2)
o5 = Order(p2, 5, c2)

c1.get_narx()
c2.get_narx()
print("Foydalanuvchi daromadi: ", u2.get_daromad())
