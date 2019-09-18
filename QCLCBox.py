import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QRadioButton, QComboBox, QLabel, QLineEdit
from PyQt5.QtCore import Qt

class QCheck(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # line edit
        self.editLabel = QLabel(self)
        self.editLabel.move(29, 200)

        qle = QLineEdit(self)
        qle.move(29, 220)
        qle.textChanged[str].connect(self.onChanged)

        #--------------------------------------------------

        # combo box
        self.lbl = QLabel('option1', self)
        self.lbl.move(29, 150)

        comboBox = QComboBox(self)
        comboBox.addItem('option1')
        comboBox.addItem('option2')
        comboBox.addItem('option3')
        comboBox.addItem('option4')
        comboBox.move(29, 170)

        # 옵션을 선택하면 onActivated() 메서드 호출
        comboBox.activated[str].connect(self.onActivated)

        #--------------------------------------------------

        # radio button
        rbtn1 = QRadioButton('radio Button1', self)
        rbtn1.move(29, 50)
        rbtn1.setChecked(True)
        
        rbtn2 = QRadioButton('radio Button2', self)
        rbtn2.move(29, 70)
        rbtn2.setChecked(True)

        #--------------------------------------------------

        # checkbox
        cb = QCheckBox('show title', self)
        cb.move(29, 20)
        cb.toggle() # 체크 박스의 default값은 off이기 때문에 toggle()을 사용하여 on의 상태로 전환
        cb.stateChanged.connect(self.changeTitle)

        #--------------------------------------------------

        self.setWindowTitle('QCheckBox')
        self.setGeometry(300, 300, 300, 300)
        self.show()

    def changeTitle(self, state):

        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle(' ')
    
    
    def onActivated(self, text):
        # adjustSize() : 라벨의 크기 자동 조절
        self.lbl.setText(text)
        self.lbl.adjustSize()
    
    def onChanged(self, text):
        self.editLabel.setText(text)
        self.editLabel.adjustSize()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = QCheck()
    sys.exit(app.exec_())
