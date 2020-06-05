import sys, threading, time, random
from PyQt5.QtWidgets import QWidget, QApplication, QProgressBar, QVBoxLayout, QHBoxLayout, QPushButton

s = threading.Semaphore(3)

class thr(threading.Thread):
    def __init__(self, pBar):
        super().__init__()
        self.pBar = pBar
    
    def run(self):
        s.acquire()
        for v in range(1, 101):
            self.pBar.setValue(v)
            time.sleep(random.randint(1,20)/500)
        s.release()
    
class main(QWidget):
    def __init__(self):
        super().__init__()
        self.lst = []
        self.lstThr = []
        self.vBox = QVBoxLayout(self)
        self.hBox = QHBoxLayout(self)
        self.btn1 = QPushButton("보통")
        self.btn2 = QPushButton("쓰레드")
        self.btn3 = QPushButton("초기화")

        self.setUi()
        self.setSlot()
    
    def setUi(self):
        self.setGeometry(500, 300, 400, 350)
        for i in range(10):
            self.lst.append(QProgressBar(self))
            self.vBox.addWidget(self.lst[i])
        self.hBox.addWidget(self.btn1)
        self.hBox.addWidget(self.btn2)
        self.hBox.addWidget(self.btn3)
        self.vBox.addWidget(self.btn1)
        self.vBox.addWidget(self.btn2)
        self.vBox.addWidget(self.btn3)
        self.setLayout(self.vBox)
        self.show()

    def setSlot(self):
        self.btn1.clicked.connect(self.normal)
        self.btn2.clicked.connect(self.thrMode)
        self.btn3.clicked.connect(self.reset)

    def normal(self):
        for i in range(10):
            for v in range(101):
                self.lst[i].setValue(v)
                time.sleep(0.007)
    
    def thrMode(self):
        for i in range(10):
            self.lstThr.append(thr(self.lst[i]))
            self.lstThr[-1].start()
        for k in self.lstThr:
            k.join()
        
    def reset(self):
        for i in range(10):
            self.lst[i].setValue(0)
    
app = QApplication([])
ex = main()
sys.exit(app.exec_())

