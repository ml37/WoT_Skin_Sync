from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
import sys
form_class = uic.loadUiType("SyncTank.ui")[0]


f = open('ClientLocation.inf', 'r')
client_location = f.readline()
print(client_location)
print(f)
#for문으로 readline으로 한줄씩 읽어서 행렬로 저장
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
    
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
    sys.exit()