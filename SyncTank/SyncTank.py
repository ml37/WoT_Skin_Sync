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
        self.listWidget.itemClicked.connect(self.on_item_clicked)
    def load_skin_list(self):
        f = open('SyncTank\Skinlist.inf', 'r')
        lines = f.readlines()
        for i in lines[0:]:
            i = i.strip()
            text = i.split('_')
            print(text[0])
            print(i)
            self.listWidget.addItem(i)
            self.label.setText('Total ' + str(self.listWidget.count()) + ' Skins')
        print('@'*50)
        f.close()
    def on_item_clicked(self, item):
        text = item.text().split('_')
        print(text[0])
        print(len(text))
        wa = ''
        for i in range(1,len(text)):
            wa = wa + text[i] + ' '
        self.number.setText(text[0])
        self.name.setText(wa)
        print(wa)
        #text[1:len(text)])
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
    sys.exit()