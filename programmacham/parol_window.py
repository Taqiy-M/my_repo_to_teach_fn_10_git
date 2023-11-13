from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QLineEdit, QLabel
password = "qwerty12345"

class PWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.le = QLineEdit()
        self.le.setPlaceholderText("password")
        self.le.setEchoMode(QLineEdit.Password)
        self.la = QLabel()
        btn = QPushButton("Enter")
        btn.clicked.connect(self.enter_clicked)
        vl = QVBoxLayout()
        vl.addWidget(self.le)
        vl.addWidget(btn)
        vl.addWidget(self.la)
        q = QWidget()
        q.setLayout(vl)
        self.setCentralWidget(q)

    def enter_clicked(self):
        if self.le.text() == password:
            print("SUCCESS")
            self.la.setText("SUCCESS ✅")
        else:
            self.la.setText("Parol notog'ri kiritildi!!!!!")



