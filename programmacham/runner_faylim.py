from PyQt5.QtWidgets import QApplication
from asosiy_windowim import MWindow
from parol_window import PWindow

app = QApplication([])


w = MWindow()
w.show()
app.exec()
