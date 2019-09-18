import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QGridLayout, QLineEdit, QTextEdit)

class QGrid(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
    
    def initUI(self):

        # grid 예제
        grid = QGridLayout()
        self.setLayout(grid)

        # addWidget(추가할 위젯, 행번호, 열번호)
        grid.addWidget(QLabel('Title: '), 0, 0) 
        grid.addWidget(QLabel('Author: '), 1, 0)
        grid.addWidget(QLabel('Review: '), 2, 0)

        grid.addWidget(QLineEdit(), 0, 1)
        grid.addWidget(QLineEdit(), 1, 1)
        grid.addWidget(QTextEdit(), 2, 1) # 여러줄의 텍스트 수정 가능

        self.setWindowTitle('QGridLayout')
        self.setGeometry(300, 300, 300, 300)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = QGrid()
    sys.exit(app.exec_())