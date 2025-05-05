from PyQt5.QtWidgets import QLabel,QDesktopWidget,QMainWindow
from PyQt5.QtCore import Qt,QPoint
from PyQt5.QtGui import QWindow,QCursor
import sys

class ControlLabel(QLabel):

    def __init__(self, parent=None):
        super(ControlLabel, self).__init__(parent)
        # other initializations...

    def enterEvent(self, QEvent):
        # here the code for mouse hover
        self.setStyleSheet("background-color:rgb(100,100,100);")
        pass

    def leaveEvent(self, QEvent):
        # here the code for mouse leave
        self.setStyleSheet("background-color:rgb(112,112,112);")
        pass


class ExitSystemm(QLabel):

    def __init__(self, parent=None):
        super(ExitSystemm, self).__init__(parent)
        # other initializations...

    def enterEvent(self, QEvent):
        # here the code for mouse hover
        self.setStyleSheet("background-color:rgb(100,100,100);")
        pass

    def leaveEvent(self, QEvent):
        # here the code for mouse leave
        self.setStyleSheet("background-color:rgb(112,112,112);")
        pass

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            sys.exit()



class Form(QMainWindow):
    def __init__(self):
        super().__init__()

        # window Options
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setFixedSize(400,400)
        #self.setWindowState(self.windowState() & Qt.WindowMinimized | Qt.WindowActive)
            

        # TitleBar
        self.titleBar = QLabel(self)
        self.titleBar.setStyleSheet("background-color:rgb(112,112,112)")
        self.titleBar.resize(400,30)
        self.titleBar.mousePressEvent = self.PressEvent
        self.titleBar.mouseMoveEvent = self.MoveEvent   

        exit_lbl_btn = ExitSystemm(self)
        exit_lbl_btn.setText("   X")
        exit_lbl_btn.resize(35,30)
        exit_lbl_btn.move(370,0)

        self.minimize_lbl_btn = ControlLabel(self)
        self.minimize_lbl_btn.installEventFilter(self)
        self.minimize_lbl_btn.setText("   --")
        self.minimize_lbl_btn.resize(35,30)
        self.minimize_lbl_btn.move(330,0)
        self.minimize_lbl_btn.mousePressEvent = self.MinimumStat


    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def PressEvent(self, event):
        self.oldPos = event.globalPos()

    def MoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

        #////////////////////////

    def MinimumStat(self,event):
        self.setWindowState(self.activateWindow() | QWindow.Minimized)

    

        # windowTitle_lbl = QLabel(self)
        # windowTitle_lbl.setText("Margin calculator")



        # label
    #     materialSize_lbl = QLabel(self)
    #     materialSize_lbl.setText("Material Size: ")
    #     mediaSize_lbl = QLabel(self)
    #     mediaSize_lbl.setText("Media Size: ")
    #     self.result_lbl = QLabel(self)
    #     self.result_lbl.setText("Null")

    #     # textBox
    #     self.materialSize_txtBox = QLineEdit(self)
    #     self.mediaSize_txtBox = QLineEdit(self)

    #     # button
    #     calc_btn = QPushButton("Calc",self)
    #     calc_btn.clicked.connect(self.calculateMargin)

    #     # layout
    #     self.materialSize_txtBox.move(100,61)

    # def calculateMargin(self):
    #     materialsize = self.materialSize_txtBox.text()
    #     mediasize = self.mediaSize_txtBox.text()
    #     calc = ((float(materialsize) - float(mediasize))/2)*10
    #     self.result_lbl.setText(f"{str(calc)} mm")

        
    

    
        
