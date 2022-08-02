from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
import sys
import os
form_class = uic.loadUiType("SyncTank.ui")[0]

print(os.listdir())
f = open('SyncTank\ClientLocation.inf', 'r')
client_location = f.readline()
print(client_location)
print(f)
f.close()

#for문으로 readline으로 한줄씩 읽어서 행렬로 저장
#read "SyncTank\Skinlist.inf", readlines(), each one line and sort with list
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.load_skin_list()
        self.btn_load.clicked.connect(self.load_skin_list)
        self.comboBox.currentIndexChanged.connect(self.on_comboBox_changed)
    def load_skin_list(self):
        f = open('SyncTank\Skinlist.inf', 'r')
        lines = f.readlines()
        for i in lines[0:]:
            i = i.strip()
            text = i.split('_')
            print(text[0])
            print(i)
            self.comboBox.addItem(i)
            self.listView.addItem(i)
        print('@'*50)
        f.close()
    def on_comboBox_changed(self):
        print(f'comboBox changed : {self.comboBox.currentText()}')
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
    sys.exit()