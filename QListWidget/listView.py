from PyQt5.QtWidgets import QWidget, QListWidget, QApplication

class Test(QWidget):
    def __init__(self):
        super().__init__()
        self.list = QListWidget(self)
        for s in ['첫번째', '두번째', '세번째']:
            self.list.addItem(s)
        self.list.currentItemChanged.connect(self.updateMe)
        self.setGeometry(300, 300, 200, 100)
        self.show()

#    def updateMe(self, item):    # this also works
#        print(item.text())

    def updateMe(self, curr, prev):
        if prev:
            print(f'curr={curr.text()}, prev={prev.text()}')
        else:
            print(f'curr={curr.text()}, prev=None')

if __name__ == "__main__":
    app = QApplication([])
    ex = Test()
    app.exec_()