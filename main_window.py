from PyQt5.QtWidgets import QLabel,QDesktopWidget,QMainWindow,QLineEdit,QPushButton
from PyQt5.QtCore import Qt,QPoint
from PyQt5.QtGui import QFont
import pyperclip
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
        self.titleBar.setStyleSheet("background-color:rgb(112,112,112);" \
        "color: white;" \
        "font: 15px;")
        self.titleBar.resize(400,30)
        self.titleBar.setText("  Margin Calculator")
        self.titleBar.mousePressEvent = self.PressEvent
        self.titleBar.mouseMoveEvent = self.MoveEvent   

        # Exit Button
        exit_lbl_btn = ExitSystemm(self)
        exit_lbl_btn.setText("   X")
        exit_lbl_btn.resize(35,30)
        exit_lbl_btn.move(370,0)

        # Minimize Button
        self.minimize_lbl_btn = ControlLabel(self)
        self.minimize_lbl_btn.installEventFilter(self)
        self.minimize_lbl_btn.setText("   --")
        self.minimize_lbl_btn.resize(35,30)
        self.minimize_lbl_btn.move(330,0)
        self.minimize_lbl_btn.mousePressEvent = self.MinimumState

        # label
        materialSize_lbl = QLabel(self)
        materialSize_lbl.setText("عرض رول")
        materialSize_lbl.move(250,70)
        materialSize_lbl.setStyleSheet("font: 20px;" \
        "font-family: B Koodak")

        mediaSize_lbl = QLabel(self)
        mediaSize_lbl.setText("عرض کار")
        mediaSize_lbl.move(250,120)
        mediaSize_lbl.setStyleSheet("font: 20px;" \
        "font-family: B Koodak")

        margin_lbl = QLabel(self)
        margin_lbl.setText("مارجین")
        margin_lbl.move(250,170)
        margin_lbl.setStyleSheet("font: 20px;" \
        "font-family: B Koodak")

        self.result_lbl = QLabel(self)
        self.result_lbl.setText("Null")
        self.result_lbl.move(100,250)
        self.result_lbl.setFixedSize(100,80)
        self.result_lbl.setStyleSheet("font: 20px;" \
        "background-color: rgb(234,213,100);" \
        "margin-left: 0px;" \
        "margin-right: 0px;" \
        "text-align: center;" \
        "padding-left: 20px")
    

        # textBox
        self.materialSize_txtBox = QLineEdit(self)
        self.materialSize_txtBox.move(100,70)

        self.mediaSize_txtBox = QLineEdit(self)
        self.mediaSize_txtBox.move(100,120)

        self.margin_txtBox = QLineEdit(self)
        self.margin_txtBox.move(100,170)

        # button
        calc_btn = QPushButton("محاسبه",self)
        calc_btn.setStyleSheet("font: 20px;" \
        "font-family: B Koodak")
        calc_btn.move(250,250)
        calc_btn.clicked.connect(self.calculateMargin)

        calc_btn = QPushButton("کپی",self)
        calc_btn.setStyleSheet("font: 20px;" \
        "font-family: B Koodak")
        calc_btn.move(250,300)
        calc_btn.clicked.connect(self.copyToClipboard)


    def calculateMargin(self):
        materialsize = self.materialSize_txtBox.text()
        mediasize = self.mediaSize_txtBox.text()
        margin = self.margin_txtBox.text()
        calc = (((float(materialsize) - float(mediasize))/2)+float(margin))*10
        self.result_lbl.setText(f"{str(calc)} mm")

    def copyToClipboard(self):
        pyperclip.copy(self.result_lbl.text()[:-5])

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

    def MinimumState(self,event):
        self.showMinimized()
    

    
        
