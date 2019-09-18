# 모듈 가져오기(import)
## import 모듈                  : 모듈 전체를 불러옴
## from 모듈 import 변수나 함수  : 모듈 내에서 필요한 것만 가져옴
# sys : 변수와 함수를 직접 제어해주는 모듈
# 기본적인 ui 구성요소를 제공하는 위젯은 PyQt5.QtWidgets 모듈에 포함
# PyQt5의 이벤트 처리 : 시그널 & 슬롯 메커니즘 

# Main Window
    ## QMenuBar, QToolBar, QDockWidget, QStatusBar를 위한 고유의 레이아웃을 가짐
    ## 가운데 영역에 중심위젯(Central widget)을 위한 영역이 있다.

# 시간관련 : https://wikidocs.net/22074

# 레이아웃(절대적배치)
## 1. 창의 크기를 조절해도 위젯의 크기와 위치는 변하지 않는다.
## 2. 다양한 플랫폼에서 어플리케이션이 다르게 보일 수 있다.
## 3. 폰트를 바꾸면 레이아웃이 망가질 수 있다.
## 4. 레이아웃을 바꾸고 싶다면 완전히 새로 고쳐야 하며, 이는 매우 번거로움.

# 박스 레이아웃
## 1. QHBoxLayout: 여러 위젯을 수평으로 정렬하는 레이아웃
##                  QHBoxLayout 생성자는 수평의 박스를 하나 만드는데, 다른 레이아웃 박스를 넣을 수도 있고, 위젯을 배치할 수도 있다.
## 2. QVBoxLayout: 여러 위젯을 수직으로 정렬하는 레이아웃
##                  QVBoxLayout 생성자는 수직의 박스를 하나 만드는데, 다른 레이아웃 박스를 넣을 수도 있고, 위젯을 배치할 수도 있다.

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QToolTip,QMainWindow, QAction, qApp, QDesktopWidget,QLabel, QHBoxLayout, QVBoxLayout)   # ui 요소
from PyQt5.QtGui import QIcon # icon
from PyQt5.QtCore import QCoreApplication # console 응용 프로그램
from PyQt5.QtCore import QDate, Qt # 날짜 출력
from PyQt5.QtGui import QFont


# 클래스 이름의 첫 문자는 대문자
# class App(QWidget): # 자식클래스(부모클래스)
class App(QMainWindow): # Main Window : 메인창(메뉴바, 툴바, 상태바)
    def __init__(self):
        # super() : 자식 클래스에서 부모클래스의 내용을 사용하고 싶을 때
        super().__init__()

        self.date = QDate.currentDate()
        self.initUI()

    def initUI(self):
        ## 수직배열(QVBoxLayout), 수평배열(QHBoxLayout)
        # addStretch(1) : 빈공간 만들기          
        # QMainWindow에서는 QVBoxLayout, QHBoxLayout를 사용하지 못한다.
        ## QMainWindow 자체의 레이아웃 사용
        okButton = QPushButton('OK')
        cancelButton = QPushButton('Cancel')

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(3)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)

        #-------------------------------------------------

        # 라벨의 위치
        label1 = QLabel('Label1', self)
        label1.move(200, 150)

        #-------------------------------------------------

        ## DefaultLocaleLongDate : 2019년 9월 18일 수요일
        ## ISODate : 2019-09-18
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate)) 

        #-------------------------------------------------

        # menu bar: 메뉴바 생성
        exitAction = QAction(QIcon('img/exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q') # 단축키 설정
        exitAction.setStatusTip('Exit application') # 상태바에 나타낼 것
        ## triggered: 생성된 시그널
        ## exitAction을 선택했을 때 생성된(triggered) 시스널이 QApplication 위젯의 quit()메서드에 연결 & 종료
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        # 첫번째 메뉴바 생성(File)
        menubar = self.menuBar()    # 메뉴바 생성
        menubar.setNativeMenuBar(False)     # macOS & Windows환경에서 동일한 결과
        fileMenu = menubar.addMenu('&File') # & : 단축키 설정(ctrl+F)
        fileMenu.addAction(exitAction)

        # 두번째 메뉴바 생성(아이콘)
        # self.toolbar = self.addToolBar('Exit')
        # self.toolbar.addAction(exitAction)

        # -------------------------------------------------

        # tooltip: 아래쪽 상태바 생성
            ## showMessage(): 상태바에 텍스트를 표시, 텍스트가 표시되는 시간 설정 가능
            ## clearMessage(): 텍스트가 사라짐
            ## currentMessage(): 현재 상태바에 표시되는 메시지 텍스트를 가지고 올때
            ## QStatusBar 클래스: 상태바에 표시되는 메세지가 바뀔 때 마다 messageChanged() 시그널 발생
        # self.statusBar().showMessage('Ready')

        # 툴팁 생성
            ## setFont: font의 글꼴과 font-size를 나타냄
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('이것은 툴팁을 나타내는 것')
        toolTipBtn = QPushButton('Button', self)
        toolTipBtn.setToolTip('이것은 <b>버튼의 툴팁</b>')
        toolTipBtn.move(50, 100)
        toolTipBtn.resize(toolTipBtn.sizeHint())

        #-------------------------------------------------

        # btn 관련(Quit 버튼 만들기)
            ## btn은 QPushButton 클래스의 인스턴스
            ## QPushButton('버튼에 표시될 텍스트', 버튼이 위치할 부모 위젯)
            ## QPushButton() : 생성자
            ## btn을 클릭하면 clicked 시그널 생성
        btn = QPushButton('Quit', self)
        btn.move(50, 70)
        btn.resize(btn.sizeHint()) # sizeHint() : 버튼을 적절한 크기
        ## instance() 메서드 : 현재 인스턴스 반환
        ## clicked 시그널 -- quit() 메서드 연결
        ## 발신자 : btn , 수신자 : 객체(app)
        btn.clicked.connect(QCoreApplication.instance().quit)
        
        ## 스타일 설정
        btn.setStyleSheet("color: red;"
                            "border-color: black;"
                            "border-width: 2px;"
                            "border-style: solid;"
                            "border-radius: 30px;")
        
        #-------------------------------------------------

        self.setWindowTitle('첫번째 앱') # 타이블바
        self.setWindowIcon(QIcon('img/web.png')) # 아이콘 설정

        self.setGeometry(300, 300, 300, 200) # 창의 위치와 크기 설정(move, resize)
        # self.move(300, 300)             # 위젯을 위치
        # self.resize(400, 200)           # 위젯의 크기

        self.center()                   # 화면 가운데에 위치하기 위해 center()메소드 수행
        self.show()                     # 보여주기

    # 창이 화면 정가운데 위치
    def center(self):
        # frameGeometry(): 창의 위치와 크기 정보 가져옴
        qr = self.frameGeometry()
        # 사용하는 모니터 화면의 가운데 위치를 파악
        cp = QDesktopWidget().availableGeometry().center()
        # 창의 직사각형 위치를 화면의 중심의 위치로 이동
        qr.moveCenter(cp)
        # 현재의 창(self)을 화면의 중심을 이동했던 직사각형(qr)의 위치로 이동
        self.move(qr.topLeft())
        

# if __name__ == '__main__': 이파일을 실행했을 때만 이 부분이 실행되고, 다른 파일에서 이 모듈을 불러서 사용했을 때는 실행문이 거짓이 된다.
if __name__ == '__main__':              # __name__ : 현재의 모듈 이름이 저장되는 내장 변수
    app = QApplication(sys.argv)        # 모든 PyQt5 어플리케이션은 객체를 생성
    ex = App()
    sys.exit(app.exec_())