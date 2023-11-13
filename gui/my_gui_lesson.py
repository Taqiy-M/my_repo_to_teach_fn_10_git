# GUI
# UI/UX
# TZ - Texnicheskiy Zadaniya
# TT - Technical Task
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import QApplication, QWidget, \
#     QLineEdit, QTextEdit, QPushButton, QMainWindow, QLabel, QVBoxLayout
#
# app = QApplication([])

# le = QLineEdit()
# pb = QPushButton()
# te = QTextEdit()
# w = QWidget()
# le.show()
# pb.show()
# te.show()
# w.show()
#
#
# app.exec()

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Hello World!!")
#         b = QPushButton("Meni Bosma!!!")
#         self.setCentralWidget(b)
#
#
#
# w = MainWindow()
# w.show()
# class Main(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Asosiy Menyu")
#         a = QTextEdit()
#         self.setCentralWidget(a)
#         # self.setFixedSize(300, 300)
#         # self.setMinimumSize(400, 300)
#         # self.setMaximumSize(600, 400)
#         # self.setMaximumHeight(400)
#
#
# c = Main()
# c.show()



# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.bosildi = False
#         self.setWindowTitle("My Signal receiver app!")
#         self.b = QPushButton("Olg'a!")
#         self.b.clicked.connect(self.tugma_bosildi)
#         # b.released.connect(self.b_bosildi)
#         self.b.setCheckable(True)
#         self.setCentralWidget(self.b)
#         self.windowTitleChanged.connect(self.hello)
#
#
#     def hello(self, w):
#         print(f"Oynaning nomi o'zgartirildi! Yangi nom: {w}")
#
#     def tugma_bosildi(self):
#         self.b.setText("Bosildi!!!")
#         self.b.setEnabled(False)
#         self.setWindowTitle("Dastur endi ishlamaydi!")
#
#
#     # def b_bosildi(self, a):
#     #     print("B Clicked!!!!!!")
#     #     if a:
#     #         print("Bosildi.")
#     #     else:
#     #         print("Qo'yib yuborildi.")

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("My App")
#         self.setMouseTracking(True)
#         self.label = QLabel("Bu shunchaki yozuv!")
#         self.setCentralWidget(self.label)
        # self.inp = QLineEdit()
        # self.inp.textChanged.connect(self.yozuv)
        #
        # layout = QVBoxLayout()
        # layout.addWidget(self.inp)
        # layout.addWidget(self.lab)
        # container = QWidget()
        # container.setLayout(layout)
        # self.setCentralWidget(container)

    # def mousePressEvent(self, e):
    #     if e.button() == Qt.LeftButton:
    #         # handle the left-button press in here
    #         self.label.setText("mousePressEvent LEFT")
    #
    #     elif e.button() == Qt.MiddleButton:
    #         # handle the middle-button press in here.
    #         self.label.setText("mousePressEvent MIDDLE")
    #
    #     elif e.button() == Qt.RightButton:
    #         # handle the right-button press in here.
    #         self.label.setText("mousePressEvent RIGHT")
    #
    # def mouseReleaseEvent(self, e):
    #     if e.button() == Qt.LeftButton:
    #         self.label.setText("mouseReleaseEvent LEFT")
    #
    #     elif e.button() == Qt.MiddleButton:
    #         self.label.setText("mouseReleaseEvent MIDDLE")
    #
    #     elif e.button() == Qt.RightButton:
    #         self.label.setText("mouseReleaseEvent RIGHT")
    #
    # def mouseDoubleClickEvent(self, e):
    #     if e.button() == Qt.LeftButton:
    #         self.label.setText("mouseDoubleClickEvent LEFT")
    #
    #     elif e.button() == Qt.MiddleButton:
    #         self.label.setText("mouseDoubleClickEvent MIDDLE")
    #
    #     elif e.button() == Qt.RightButton:
    #         self.label.setText("mouseDoubleClickEvent RIGHT")
    # def yozuv(self, y):
    #     print(f"O'zgargan yozuv: {y}")
    #     self.lab.setText(y)









# c = MainWindow()
# c.show()
# app.exec()
#





import sys

from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets App")

        layout = QVBoxLayout()
        widgets = [
            QCheckBox,
            QComboBox,
            QDateEdit,
            QDateTimeEdit,
            QDial,
            QDoubleSpinBox,
            QFontComboBox,
            QLCDNumber,
            QLabel,
            QLineEdit,
            QProgressBar,
            QPushButton,
            QRadioButton,
            QSlider,
            QSpinBox,
            QTimeEdit,
        ]

        for w in widgets:
            layout.addWidget(w())

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()











