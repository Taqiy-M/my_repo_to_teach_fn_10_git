from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget

from programmacham.parol_window import PWindow


class MWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.p = None
        admin = QPushButton("Admin")
        admin.clicked.connect(self.admin_clicked)
        user = QPushButton("User")
        user.clicked.connect(self.user_clicked)
        vl = QVBoxLayout()
        vl.addWidget(admin)
        vl.addWidget(user)
        q = QWidget()
        q.setLayout(vl)
        self.setCentralWidget(q)

    def user_clicked(self):
        print("User clicked!!!!")

    def admin_clicked(self):
        # if self.p is None:
        self.p = PWindow()
        self.p.show()

        print("Admin clicked!!!!!")

