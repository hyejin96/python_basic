import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout)
from PyQt5.QtGui import QIcon, QPixmap

class QPush(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
    
    def initUI(self):

        # QPushButton
        ## setCheckable(true) : true: 누른 상태, false : 그렇지 않은 상태
        ## toggle : 상태를 바꾼다.
        ## setEnabled(true) : False: 버튼 사용할 수 없음.
        ## setText() : 버튼에 표시될 텍스트 설정
        pbtn1 = QPushButton('&Button1', self)
        pbtn1.setCheckable(True)
        pbtn1.toggle()  

        pbtn2 = QPushButton(self)
        pbtn2.setText('Button&2')

        pbtn3 = QPushButton('Button3', self)
        pbtn3.setEnabled(False)

        vbox = QVBoxLayout()
        vbox.addWidget(pbtn1)
        vbox.addWidget(pbtn2)
        vbox.addWidget(pbtn3)

        self.setLayout(vbox)

        self.setWindowTitle('QGridLayout')
        self.setGeometry(300, 300, 300, 300)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = QPush()
    sys.exit(app.exec_())