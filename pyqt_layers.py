# from time import sleep
#
# from PyQt5.QtWidgets import *
# app = QApplication([])
#
#
# class Window(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         # self.a = QPushButton("Tugma")
#         self.te = QLineEdit()
#         self.te.setPlaceholderText("Nimadir Kiriting.")
#         # self.i = 0
#         self.te.textChanged.connect(self.text_ozgardi)
#         # self.a.clicked.connect(self.a_clicked)
#         self.setCentralWidget(self.te)
#
#
#     def text_ozgardi(self, a):
#         print(a)
#
#     def a_clicked(self):
#         self.i += 1
#         self.setWindowTitle(f"{self.i}")
#         self.a.setText(f"{self.i}")
#         print(f"Bosildi!!!!! {self.i}")
#         if self.i == 10:
#
#             self.a.setEnabled(False)
#
#
#
#
#
# class Window(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.s = QSlider()
#         self.i = 0
#         self.s.valueChanged.connect(self.v_ch)
#         self.s.sliderPressed.connect(self.s_pressed)
#         self.s.setMinimum(1)
#         self.s.setMaximum(100)
#         self.setCentralWidget(self.s)
#
#     def s_pressed(self):
#         for i in range(100):
#             sleep(1)
#             self.s.setValue(i)
#         # self.i += 10
#
#
#
#     def v_ch(self, a):
#         print(a)
#
#
# w = Window()
# w.show()
# app.exec()
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import *
app = QApplication([])


class Color(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


class Murodali(QMainWindow):
    def __init__(self):
        super().__init__()
        v_l = QHBoxLayout()
        a = Color("red")
        b = Color("cyan")
        c = Color("yellow")
        d = Color("violet")
        v_l.addWidget(a)
        v_l.addWidget(b)
        v_l.addWidget(c)
        v_l.addWidget(d)
        q = Color("green")
        q.setLayout(v_l)

        q1 = Color("purple")

        l = QHBoxLayout()
        a1 = Color("#787475")
        b1 = Color("#e1e920")
        l.addWidget(a1)
        l.addWidget(b1)
        q2 = QWidget()
        q2.setLayout(l)

        v_l_new = QVBoxLayout()
        v_l_new.addWidget(q)
        v_l_new.addWidget(q1)
        v_l_new.addWidget(q2)
        wid = QWidget()
        wid.setLayout(v_l_new)


        self.setCentralWidget(wid)


class Shohruh(QMainWindow):
    def __init__(self):
        super().__init__()

        c1 = Color("green")
        c2 = Color("yellow")
        c3 = Color("#a58901")
        c4 = Color("#99e3FF")
        hl = QHBoxLayout()
        hl.addWidget(c1)
        hl.addWidget(c2)
        hl.addWidget(c3)
        hl.addWidget(c4)
        w = QWidget()
        w.setLayout(hl)


        d1 = Color("brown")
        d2 = Color("#FF98E1")
        h2 = QHBoxLayout()
        h2.addWidget(d1)
        h2.addWidget(d2)
        w1 = QWidget()
        w1.setLayout(h2)


        e1 = Color("green")
        e2 = Color("red")
        e3 = Color("yellow")
        h3 = QHBoxLayout()
        h3.addWidget(e1)
        h3.addWidget(e2)
        h3.addWidget(e3)
        w2 = QWidget()
        w2.setLayout(h3)


        ver = QVBoxLayout()
        ver.addWidget(w)
        ver.addWidget(w1)
        ver.addWidget(w2)
        ver_wid = QWidget()
        ver_wid.setLayout(ver)

        ver2 = QVBoxLayout()
        ver2.addWidget(Color("grey"))
        ver2.addWidget(Color("orange"))
        ver2.addWidget(Color("blue"))
        ver_wid1 = QWidget()
        ver_wid1.setLayout(ver2)

        eng_kotta_lay = QHBoxLayout()
        eng_kotta_lay.addWidget(ver_wid1)
        eng_kotta_lay.addWidget(ver_wid)
        eng_kotta_wid = QWidget()
        eng_kotta_wid.setLayout(eng_kotta_lay)
        self.setCentralWidget(ver_wid)


class Tillayev(QMainWindow):
    def __init__(self):
        super().__init__()
        a1 = Color("red")
        a2 = Color("cyan")
        l1 = QHBoxLayout()
        l1.addWidget(a1)
        l1.addWidget(a2)
        w1 = QWidget()
        w1.setLayout(l1)


        l2 = QVBoxLayout()
        b1 = Color("key")
        b2 = Color("green")
        b3 = Color("orange")
        l2.addWidget(b1)
        l2.addWidget(b2)
        l2.addWidget(b3)
        w2 = QWidget()
        w2.setLayout(l2)


        ma = QHBoxLayout()
        ma.addWidget(w1)
        ma.addWidget(w2)
        wid = QWidget()
        wid.setLayout(ma)
        self.setCentralWidget(wid)


class TermsConditions(QMainWindow):
    def __init__(self):
        super().__init__()
        a = QRadioButton("Salom")
        b = QRadioButton("Alik")
        c = QRadioButton("Privet")
        a.clicked.connect(self.arbtn_clicked)
        b.clicked.connect(self.brbtn_clicked)
        c.clicked.connect(self.crbtn_clicked)
        self.radio = 0
        # a.stateChanged.connect(self.a_changed)
        # self.b = QPushButton("Ro'yxatdan O'tish")
        # self.b.setEnabled(False)
        vl = QHBoxLayout()
        vl.addWidget(a)
        vl.addWidget(b)
        vl.addWidget(c)
        w = QWidget()
        w.setLayout(vl)
        self.setCentralWidget(w)

    def arbtn_clicked(self):
        self.radio = 1
        print("Birinchisi")

    def brbtn_clicked(self):
        self.radio = 2
        print("Ikkinchisi")

    def crbtn_clicked(self):
        self.radio = 3
        print("Uchinchisi")

    def a_changed(self, a):
        self.b.setEnabled(a)


m = TermsConditions()
m.show()

app.exec()






