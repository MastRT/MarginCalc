from PyQt5.QtWidgets import QApplication,QMainWindow
import sys
from main_window import Form



app = QApplication(sys.argv)

Window = Form()
Window.setFixedSize(400,400)
Window.show()
app.exec_()