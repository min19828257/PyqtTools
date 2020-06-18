#########################################################################
# Pyqt에서 서브 화면을 만들때 사용되는 클래스 방식
#########################################################################

# import sys
# from PyQt5.QtWidgets import *
# from PyQt5 import uic

# form_class = uic.loadUiType("메인 ui의 절대값 주소")[0]  #메인 화면ui

# class findWindow(QDialog):
#     def __init__(self, parent):
#         super(findWindow, self).__init__(parent)
#         uic.loadUi("서브 ui의 절대 값 주소")

# class WindowClass(QMainWindow, form_class):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)
        
#         findWindow(self)

#########################################################################
# Pyqt에서 서브 화면을 만들때 부모 클래스 사용없이 생성
#########################################################################

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class1 = uic.loadUiType("main_window.ui")[0]
form_class2 = uic.loadUiType("new_window.ui")[0]

class NewWindow(QMainWindow, form_class2):
    def __init__(self, parent=None):
        super(NewWindow, self).__init__(parent)
        self.setupUi(self)

class MyWindow(QMainWindow, form_class1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)        
        self.pushButton.clicked.connect(self.button_clicked)

    # 버튼이 클릭될 때 새로운 창 생성
    def button_clicked(self):
        self.newWindow = NewWindow(self)
        self.newWindow.show()

app = QApplication(sys.argv)
mywindow = MyWindow()
mywindow.show()
app.exec_()