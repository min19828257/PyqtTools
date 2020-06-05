#########################################################################
# Pyqt에서 서브 화면을 만들때 사용되는 클래스 방식
#########################################################################

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("메인 ui의 절대값 주소")[0]  #메인 화면ui

class findWindow(QDialog):
    def __init__(self, parent):
        super(findWindow, self).__init__(parent)
        uic.loadUi("서브 ui의 절대 값 주소")

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)