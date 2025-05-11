from PyQt5.QtWidgets import QLabel,QDesktopWidget,QMainWindow,QLineEdit,QPushButton
from PyQt5.QtCore import Qt,QPoint
from PyQt5.QtGui import QPixmap,QIcon
import ctypes
import pyperclip
import sys

class ControlLabel(QLabel):

    def __init__(self, parent=None):
        super(ControlLabel, self).__init__(parent)
        # other initializations...

    def enterEvent(self, QEvent):
        # here the code for mouse hover
        self.setStyleSheet("background-color:#1a1a2c;" \
        "color: white;")
        pass

    def leaveEvent(self, QEvent):
        # here the code for mouse leave
        self.setStyleSheet("background-color:#24243e;" \
        "color: white;")
        pass


class ExitSystemm(QLabel):

    def __init__(self, parent=None):
        super(ExitSystemm, self).__init__(parent)
        # other initializations...

    def enterEvent(self, QEvent):
        # here the code for mouse hover
        self.setStyleSheet("background-color:#1a1a2c;" \
        "color: white;")
        pass

    def leaveEvent(self, QEvent):
        # here the code for mouse leave
        self.setStyleSheet("background-color:#24243e;" \
        "color: white;")
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
        myappid = u'Reza.Shook.MarginCalculator.v1' # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        self.setWindowIcon(QIcon("img\margin.png"))

        # Background LBL
        background_lbl = QLabel(self)
        background_lbl.setFixedSize(400,400)
        background_lbl.setStyleSheet("background-image: url(img/background.jpg);" \
        "background-repeat: no-repeat;" \
        "background-position: center;")
        background_lbl.lower()
    

        # TitleBar
        self.titleBar = QLabel(self)
        self.titleBar.setStyleSheet("background-color:#24243e;" \
        "color: white;" \
        "font: 15px;")
        self.titleBar.resize(400,30)
        self.titleBar.setText("      Margin Calculator")
        self.titleBar.mousePressEvent = self.PressEvent
        self.titleBar.mouseMoveEvent = self.MoveEvent  
        

        # Icon
        iconPic = QPixmap("img\margin.png")
        iconPic = iconPic.scaled(20, 20, Qt.KeepAspectRatio, Qt.FastTransformation)
        iconlabel = QLabel(self)
        iconlabel.setPixmap(iconPic)
        iconlabel.resize(iconPic.width(),iconPic.height())
        iconlabel.move(5,5)
         

        # Exit Button
        exit_lbl_btn = ExitSystemm(self)
        exit_lbl_btn.setText("   X")
        exit_lbl_btn.resize(35,30)
        exit_lbl_btn.move(365,0)
        exit_lbl_btn.setStyleSheet("background-color:#24243e;" \
        "color: white;")


        # Minimize Button
        self.minimize_lbl_btn = ControlLabel(self)
        self.minimize_lbl_btn.installEventFilter(self)
        self.minimize_lbl_btn.setText("   --")
        self.minimize_lbl_btn.resize(35,30)
        self.minimize_lbl_btn.move(330,0)
        self.minimize_lbl_btn.setStyleSheet("background-color:#24243e;" \
        "color: white;")
        self.minimize_lbl_btn.mousePressEvent = self.MinimumState

        # label
        materialSize_lbl = QLabel(self)
        materialSize_lbl.setText("عرض رول")
        materialSize_lbl.move(250,70)
        materialSize_lbl.setStyleSheet("font: 20px;" \
        "font-family: B Koodak;" \
        "background-color: transparent;" \
        "color:white;")

        mediaSize_lbl = QLabel(self)
        mediaSize_lbl.setText("عرض کار")
        mediaSize_lbl.move(250,120)
        mediaSize_lbl.setStyleSheet("font: 20px;" \
        "font-family: B Koodak;" \
        "color:white;")

        margin_lbl = QLabel(self)
        margin_lbl.setText("مارجین")
        margin_lbl.move(250,170)
        margin_lbl.setStyleSheet("font: 20px;" \
        "font-family: B Koodak;" \
        "color:white;")

        self.result_lbl = QLabel(self)
        self.result_lbl.setText("Null")
        self.result_lbl.move(100,250)
        self.result_lbl.setFixedSize(120,80)
        self.result_lbl.setStyleSheet("font: 20px;" \
        "background-color: transparent;" \
        "color: white;" \
        "text-align: center;" \
        "padding-left: 10px")

        # Created with love
        author_lbl = QLabel(self)
        author_lbl.setText("Created with ❤️ by Reza © 2025")
        author_lbl.move(5,373)
        author_lbl.setFixedSize(400,30)
        author_lbl.setStyleSheet("color: white;" \
        "font: 10px")
    

        # textBox
        self.materialSize_txtBox = QLineEdit(self)
        self.materialSize_txtBox.move(100,70)
        self.materialSize_txtBox.setStyleSheet("border:none;" \
        "background-color:#e2dcf5;" \
        "font: 20px;")

        self.mediaSize_txtBox = QLineEdit(self)
        self.mediaSize_txtBox.move(100,120)
        self.mediaSize_txtBox.setStyleSheet("border: none;" \
        "background-color:#e2dcf5;" \
        "font: 20px;")

        self.margin_txtBox = QLineEdit(self)
        self.margin_txtBox.move(100,170)
        self.margin_txtBox.setStyleSheet("border: none;" \
        "background-color:#e2dcf5;" \
        "font: 20px;")


        #button's style
        style = "QPushButton#copy:pressed{background-color: #7B98C1;}" \
        "QPushButton#copy{font: 20px;" \
        "font-family: B Koodak;" \
        "background-color: #24243e;" \
        "color: white;" \
        "border: none;}"

        # calculate button
        self.calc_btn = QPushButton("محاسبه",self)
        self.calc_btn.setObjectName("copy")
        self.calc_btn.setStyleSheet(style)
        self.calc_btn.move(250,250)
        self.calc_btn.clicked.connect(self.calculateMargin)

        #copt to clipboard btn
        copy_btn = QPushButton("کپی",self)
        copy_btn.setObjectName("copy")
        copy_btn.setStyleSheet(style)
        copy_btn.move(250,300)
        copy_btn.clicked.connect(self.copyToClipboard)


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
    

    
        
