import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt

class QLa(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
    
    def initUI(self):

        # setAlignment() : 수평, 수직 방향 모두 가운데 위치
        # AlignHCenter() : 수평 방향 가운데 위치
        # AlignVCenter() : 수직 방향 가운데 위치
        label1 = QLabel('First Label', self)
        label1.setAlignment(Qt.AlignCenter)
        
        label2 = QLabel('Second Label', self)
        label2.setAlignment(Qt.AlignHCenter)

        font1 = label1.font()
        font1.setPointSize(20)

        font2 = label2.font()
        font2.setFamily('Times New Roman')
        font2.setBold(True)

        label1.setFont(font1)
        label2.setFont(font2)

        layout = QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(label2)

        self.setLayout(layout)

        self.setWindowTitle('QLabel')
        self.setGeometry(300, 300, 300, 300)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = QLa()
    sys.exit(app.exec_())
