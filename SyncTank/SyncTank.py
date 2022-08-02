from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
import sys
import os
import urllib.request
import shutil
form_class = uic.loadUiType("SyncTank.ui")[0]

#print(os.listdir())
print('@'*50)
f = open('SyncTank\ClientLocation.inf', 'r')
client_location = f.readline()
print(client_location)
f.close()
print('@'*50)
DLServer = 'http://' + 'mashiro37.i234.me'
DLSkinlist = DLServer + '/WoTskin/' + 'Skinlist.inf'
DLtemp = client_location + '\\SkinTemp' + '\\PySyncTank\\ + \\DLtemp\\'
print(DLSkinlist)
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.load_skin_list()
        self.listWidget.itemClicked.connect(self.on_item_clicked)
        self.btn_download.clicked.connect(self.download)
    def load_skin_list(self):
        f = open('SyncTank\Skinlist.inf', 'r')
        lines = f.readlines()
        for i in lines[0:]:
            i = i.strip()
            text = i.split('_')
            #print(text[0])
            #print(i)
            self.listWidget.addItem(i)
            self.label.setText('Total ' + str(self.listWidget.count()) + ' Skins')
        print('@'*50)
        f.close()
    def on_item_clicked(self, item):
        text = item.text().split('_')
        wa = ''
        for i in range(1,len(text)):
            wa = wa + text[i] + ' '
        self.number.setText(text[0])
        self.name.setText(wa)
        global vehicle_number
        global vehicle_name
        vehicle_number=text[0]
        vehicle_name=wa
    def download(self): 
        print('!'*50)
        print(self.listWidget.currentItem().text())
        downloadURL = DLServer + '/WoTskin/' + 'Skin/' + vehicle_number + '.zip'
        print(downloadURL)
        urllib.request.urlretrieve(downloadURL, vehicle_number + '.zip')
        shutil.move(vehicle_number + '.zip', DLtemp)
        print('!'*50)
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
    sys.exit()