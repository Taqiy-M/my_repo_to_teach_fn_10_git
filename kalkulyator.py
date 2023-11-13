from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, \
    QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QApplication

app = QApplication([])


class MW(QMainWindow):
    def __init__(self):
        super().__init__()
        self.le = QLabel()
        self.a = 0
        self.b = 0
        self.amal = ""

        tugmalar = [["Clear", "%", "/"],
                    ["7", "8", "9", "*"],
                    ["4", "5", "6", "-"],
                    ["1", "2", "3", "+"],
                    ["0", ",", "="]
                    ]
        asosiy = QVBoxLayout()
        asosiy.addWidget(self.le)

        for i in tugmalar:
            a = QHBoxLayout()
            for j in i:
                qb = QPushButton(j)
                qb.clicked.connect(self.bosildi)
                a.addWidget(qb)
            w = QWidget()
            w.setLayout(a)
            asosiy.addWidget(w)

        asosiy_widget = QWidget()
        asosiy_widget.setLayout(asosiy)
        self.setCentralWidget(asosiy_widget)

    def bosildi(self):
        t = self.sender().text()
        if self.amal == "":
            if t.isdigit():
                self.a = self.a*10 + int(t)
                self.le.setText(str(self.a))
        else:
            if t.isdigit():
                self.b = self.b * 10 + int(t)
                self.le.setText(str(self.b))

        if t == "Clear":
            self.a = 0
            self.b = 0
            self.amal = ""
            self.le.clear()

        if t in ["/", "*", "+", "-"]:
            self.amal = t
            self.le.clear()

        if t == "=":
            self.le.setText(str(eval(str(self.a)+self.amal+str(self.b))))
            self.amal = ""
            self.a = 0
            self.b = 0


a = MW()
a.show()
app.exec()
