import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar
from PyQt5.QtCore import QBasicTimer

class QProgress(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
    
    def initUI(self):

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)

        self.btn = QPushButton('start', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)

        # QBasicTimer() : 진행 표시줄을 활성화하기 위해 타이머 객체 사용
        self.timer = QBasicTimer()
        self.step = 0

        self.setWindowTitle('progress')
        self.setGeometry(300, 300, 300, 200)
        self.show()
    
    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return
        
        self.step = self.step + 1
        self.pbar.setValue(self.step)
    
    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('start')
        else: 
            self.timer.start(100, self)
            self.btn.setText('stop')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = QProgress()
    sys.exit(app.exec_())