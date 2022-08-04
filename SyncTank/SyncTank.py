from PyQt5.QtWidgets import QPushButton, QWidget, QLabel, QApplication, QMainWindow, QFileDialog, QAction
#from PyQt5.QtCore import *
#from PyQt5.QtGui import *
from PyQt5.QtGui import QIcon
from PyQt5 import uic
import sys
import os
import urllib.request
from urllib.request import Request, urlopen
import shutil
import zipfile
import subprocess
#qPixmapVar = QPixmap()
form_class = uic.loadUiType("SyncTank.ui")[0]
FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')
DataFolder = 'c:\SyncTank'
print('@'*50)
if os.path.isdir(DataFolder) == False:
    os.mkdir(DataFolder)
if os.path.isdir(DataFolder + '\Zipmaker') == False:
    os.mkdir(DataFolder + '\Zipmaker')
if os.path.isfile(DataFolder + '\DLserver.inf') == False:
    with open(DataFolder + '\DLserver.inf', 'w') as f:
        f.write('mashiro37.i234.me')
with open(DataFolder + '\DLserver.inf', 'r') as f:
    DLServer = f.read()
    print(DLServer)
    if DLServer == 'mashiro37.i234.me':
        print('DLserver is mashiro37.i234.me')
        DLServer = 'http://' + 'mashiro37.i234.me'
    else:
        print('DLserver is other')
        print(f'Notice : DLserver is {DLServer}')
        DLServer = 'http://' + DLServer
    
if os.path.isfile(DataFolder + '\ClientLocation.inf') == False:
    print(f'{DataFolder}\ClientLocation.inf is not found')
    client_location = 'error'
else:
    with open(DataFolder + '\ClientLocation.inf', 'r') as f:
        client_location = f.readline()
        print(f'client location : {client_location}')
if os.path.isfile(DataFolder + '\Zipmaker' +'\ServerLocation.inf') == False:
    print(f'{DataFolder}\Zipmaker\ServerLocation.inf is not found')
    server_location = 'error'
else:
    with open(DataFolder + '\Zipmaker' +'\ServerLocation.inf', 'r') as f:
        server_location = f.readline()
        print(f'server location : {server_location}')
print('@'*50)
#DLServer = 'http://' + 'mashiro37.i234.me'
DLSkinlist = DLServer + '/WoTskin/' + 'PySkin/' + 'Skinlist.inf'
DLVersion = DLServer + '/WoTskin/' + 'Version.inf'
DLtemp = client_location + '\\SkinTemp' + '\\PySyncTank\\' + '\\DLtemp\\'
Unziptemp = client_location + '\\SkinTemp' + '\\PySyncTank\\' + '\\Unziptemp\\' 
ZipMaketemp = client_location + '\\SkinTemp' + '\\PySyncTank\\' + '\\ZipMaketemp\\'  
country = {'A':'american', 'GB':'british', 'Ch':'chinese', 'Cz':'czech', 'F':'french', 'G':'german', 'It':'italy', 'J':'japan', 'Pl':'poland', 'R':'russian', 'S':'sweden'}
countryimg = {'A':'usa', 'GB':'uk', 'Ch':'china', 'Cz':'czech', 'F':'france', 'G':'germany', 'It':'italy', 'J':'japan', 'Pl':'poland', 'R':'ussr', 'S':'sweden'}
print(DLSkinlist)
if os.path.isfile(DataFolder + '\Version.inf') == False:
    print('c:\SyncTank\Version.inf is not found')
    try:
        urllib.request.urlretrieve(DLVersion, DataFolder + '/Version.inf')
    except urllib.error.HTTPError as e:
        print(e.__dict__)
    except urllib.error.URLError as e:
        print(e.__dict__)
if os.path.isfile(DataFolder + '\Skinlist.inf') == False:
    print('c:\SyncTank\Skinlist.inf is not found')
    try:
        urllib.request.urlretrieve(DLSkinlist, DataFolder + '/Skinlist.inf')
    except urllib.error.HTTPError as e:
        print(e.__dict__)
    except urllib.error.URLError as e:
        print(e.__dict__)
Version = 'error'
with open(DataFolder + '\Version.inf', 'r') as f:
    Version = f.readline()
    print(f'Version : {Version}')
if client_location == 'error':
    print('client location is not found')
else:
    if os.path.isdir(client_location + '\SkinTemp') == False:   
        os.mkdir(client_location + '\\SkinTemp')
    if os.path.isdir(client_location + '\SkinTemp' + '\PySyncTank') == False:
        os.mkdir(client_location + '\\SkinTemp\\PySyncTank')
    if os.path.isdir(client_location + '\SkinTemp' + '\PySyncTank' + '\DLtemp') == False:
        os.mkdir(client_location + '\\SkinTemp\\PySyncTank\\DLtemp')
    if os.path.isdir(client_location + '\\SkinTemp' + '\\PySyncTank' + '\\Unziptemp') == False:
        os.mkdir(client_location + '\\SkinTemp\\PySyncTank\\Unziptemp')
    if Version == 'error':
        print('Version is not found')
    else:
        if os.path.isdir(client_location + '\\res_mods\\' + Version) == False:
            os.mkdir(client_location + '\\res_mods\\' + Version)
        if os.path.isdir(client_location + '\\res_mods\\' + Version + '\\vehicles') == False:
            os.mkdir(client_location + '\\res_mods\\' + Version + '\\vehicles')

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.load_skin_list()
        self.listWidget.itemClicked.connect(self.on_item_clicked)
        self.btn_download.clicked.connect(self.download)
        self.btn_opencl.clicked.connect(self.opencl)
        self.btn_openus.clicked.connect(self.openus)
        self.btn_manuallist.clicked.connect(self.manuallist)
        self.btn_all.clicked.connect(self.all)
        self.btn_cleartemp.clicked.connect(self.cleartemp)
        self.btn_openus.setEnabled(False)
        self.btn_manuallist.setEnabled(False)
        self.btn_reload.clicked.connect(self.load_skin_list)
        self.setAcceptDrops(True)
        selClientLoc = QAction('Select Game Client Location', self)
        selClientLoc.triggered.connect(self.selClientLocation)
        self.setWindowIcon(QIcon('icon.png'))
        
        selServerLoc = QAction('Select Upload Server Location', self)
        selServerLoc.triggered.connect(self.selServerLocation)
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('&Location')
        fileMenu.addAction(selClientLoc)
        fileMenu.addAction(selServerLoc)
        self.setWindowTitle('SyncTank')
        if client_location == 'error':
            fname = QFileDialog.getExistingDirectory(self, 'Select Game Client(World_of_Tanks_ASIA) Location', './')
            if fname:
                print(fname)
                f = open(DataFolder + '\ClientLocation.inf', 'w')
                f.write(fname)
                f.close()
        if server_location == 'error':
            print('auto upload disabled')
        else:
            self.btn_openus.setEnabled(True)
            self.btn_manuallist.setEnabled(True)
    
    def selClientLocation(self):
        fname = QFileDialog.getExistingDirectory(self, 'Select Game Client(World_of_Tanks_ASIA) Location', './')

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                print(data)
    def selServerLocation(self):
            fname = QFileDialog.getExistingDirectory(self, 'Select Upload Server(PySkins) Location', './')
            if fname:
                print(fname)
                f = open(DataFolder + '\Zipmaker' +'\ServerLocation.inf', 'w')
                f.write(fname)
                f.close()
    def manuallist(self):
        path = server_location
        file_list = os.listdir(path)
        file_list_py = [file for file in file_list if file.endswith(".zip")]
        f = open(server_location + '\Skinlist.inf', 'w')
        for file in file_list_py:
            file = file.replace('.zip', '')
            f.write(file + '\n')
        f.close()
    def cleartemp(self):
        print('cleartemp')
        if os.path.isdir(client_location + '\\SkinTemp' + '\\PySyncTank' + '\\DLtemp') == True:
            shutil.rmtree(client_location + '\\SkinTemp' + '\\PySyncTank' + '\\DLtemp')
            os.mkdir(client_location + '\\SkinTemp\\PySyncTank\\DLtemp')
        if os.path.isdir(client_location + '\\SkinTemp' + '\\PySyncTank' + '\\Unziptemp') == True:
            shutil.rmtree(client_location + '\\SkinTemp' + '\\PySyncTank' + '\\Unziptemp')
            os.mkdir(client_location + '\\SkinTemp\\PySyncTank\\Unziptemp')
    def load_skin_list(self):
        self.listWidget.clear()
        try:
            urllib.request.urlretrieve(DLSkinlist, DataFolder + '/Skinlist.inf')
        except urllib.error.HTTPError as e:
            print(e.__dict__)
            self.btn_download.setEnabled(False)
        except urllib.error.URLError as e:
            print(e.__dict__)
            self.btn_download.setEnabled(False)
            self.lbl_error.setText('Error!')
            self.lbl_error_2.setText(str(e.reason))
        f = open(DataFolder + '\Skinlist.inf', 'r')
        lines = f.readlines()
        for i in lines[0:]:
            i = i.strip()
            text = i.split('_')
            self.listWidget.addItem(i)
            self.label.setText('Total ' + str(self.listWidget.count()) + ' Skins')
        print('@'*50)
        f.close()
        self.lbl_Version.setText('Version : ' + Version)
        self.lbl_clientlocation.setText('Client Location : ' + client_location)
        self.lbl_serverlocation.setText('Server Location : ' + server_location)
        self.lbl_DLserver.setText('DL Server : ' + DLServer)
    def on_item_clicked(self, item):
        
        text = item.text().split('_')
        wa = ''
        for i in range(1,len(text)):
            wa = wa + text[i] + ' '
        self.number.setText(text[0])
        self.name.setText(wa)
        global vehicle_number
        global vehicle_name
        global lawname
        global vehicle_Countrycode
        global vehicle_country
        vehicle_number=text[0]
        vehicle_name=wa[0:-1]
        lawname = item.text()
        string = vehicle_number
        vehicle_Countrycode = ''.join([i for i in string if not i.isdigit()])
        vehicle_country = country[vehicle_Countrycode]
        url = 'http://tanks.gg/img/tanks/' + countryimg[vehicle_Countrycode] + '-' + lawname + '.png'
        try:
            image=Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        except urllib.error.HTTPError as e:
            print(e.__dict__)
            self.btn_download.setEnabled(False)
        except urllib.error.URLError as e:
            print(e.__dict__)
            self.btn_download.setEnabled(False)
            self.lbl_error.setText('Error!')
            self.lbl_error_2.setText(str(e.reason))
        image_data = urlopen(image).read()
        self.qPixmapWebVar = QPixmap()
        self.qPixmapWebVar.loadFromData(image_data)
        self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(360) # 480x300 320x200 360x240
        self.lbl_img.setPixmap(self.qPixmapWebVar)
        url_flag = 'http://tanks.gg/img/nations/germany.svg'
        url_flag = 'http://tanks.gg/img/nations/' + countryimg[vehicle_Countrycode] + '.svg'
        try:
            image_flag = Request(url_flag, headers={'User-Agent': 'Mozilla/5.0'})
        except urllib.error.HTTPError as e:
            print(e.__dict__)
            self.btn_download.setEnabled(False)
        except urllib.error.URLError as e:
            print(e.__dict__)
            self.btn_download.setEnabled(False)
            self.lbl_error.setText('Error!')
            self.lbl_error_2.setText(str(e.reason))
        image_data_flag = urlopen(image_flag).read()
        self.qPixmapWebVar_flag = QPixmap()
        self.qPixmapWebVar_flag.loadFromData(image_data_flag)
        self.qPixmapWebVar_flag = self.qPixmapWebVar_flag.scaledToWidth(100)
        self.lbl_img_2.setPixmap(self.qPixmapWebVar_flag)
        
        
    def download(self): 
        print('!'*50)
        print(self.listWidget.currentItem().text())
        downloadURL = DLServer + '/WoTskin/' + 'PySkin/' + lawname + '.zip'
        print(downloadURL)
        if os.path.exists(DLtemp + lawname + '.zip'):
            print('File Exists')
        else:
            try:
                urllib.request.urlretrieve(downloadURL, lawname + '.zip')
            except urllib.error.HTTPError as e:
                print(e.__dict__)
                self.btn_download.setEnabled(False)
            except urllib.error.URLError as e:
                print(e.__dict__)
                self.btn_download.setEnabled(False)
                self.lbl_error.setText('Error!')
                self.lbl_error_2.setText(str(e.reason))
            shutil.move(lawname + '.zip', DLtemp)
        zipzip = zipfile.ZipFile(DLtemp + lawname + '.zip', 'r')
        zipzip.extractall(path=Unziptemp + lawname)
        zipzip.close()
        print('!'*50)
        if os.path.exists(client_location + '/res_mods/' + Version + '/vehicles/' + vehicle_country):
            print('File Exists')
        else:
            os.mkdir(client_location + '/res_mods/' + Version + '/vehicles/' + vehicle_country)
        if os.path.exists(client_location + '/res_mods/' + Version + '/vehicles/' + vehicle_country + '/' + lawname):
            print('File Exists')
        else:
            shutil.copytree(Unziptemp + lawname, client_location + '/res_mods/' + Version + '/vehicles/' + vehicle_country + '/' + lawname)
    def all(self):
        for i in range(self.listWidget.count()):
            self.listWidget.item(i).setSelected(True)
            self.on_item_clicked(self.listWidget.item(i))
            self.download()
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()
    def dropEvent(self, event):
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        print('$'*50)
        for f in files:
            print(f)
            #f split 
            nananame = f.split('/')
            name = nananame[len(nananame)-1]
            name = name
            print(name)
            print(f)
            if server_location == 'error':
                print('auto upload disabled')
            else:
                if os.path.exists(server_location + '/' + name + '.zip') == True:
                    print(f'Upload Error File Exists {name}')
                else:
                    zipmake = zipfile.ZipFile(f + '.zip', 'w')
                    for folder, subfolders, files in os.walk(f):
                        for file in files:
                            if file.endswith('.dds'):
                                zipmake.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), f), compress_type = zipfile.ZIP_DEFLATED)
                            elif file.endswith('.psd'):
                                zipmake.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), f), compress_type = zipfile.ZIP_DEFLATED)
                    zipmake.close()
                    shutil.move(f + '.zip', server_location)
                    print(name + '.zip' + ' uploaded')
                    with open(server_location + '/Skinlist.inf', 'a') as f:
                        f.write(name + '\n')
            
            
        print('$'*50)
        self.load_skin_list()

    def opencl(self):
            # explorer would choke on forward slashes
        path = client_location.replace('/', '\\')
        path = os.path.normpath(path)
        if os.path.isdir(path):
            subprocess.run([FILEBROWSER_PATH, path])
        elif os.path.isfile(path):
            subprocess.run([FILEBROWSER_PATH, '/select,', os.path.normpath(path)])
    def openus(self):
            # explorer would choke on forward slashes
        path = server_location.replace('/', '\\')
        path = os.path.normpath(path)
        if os.path.isdir(path):
            subprocess.run([FILEBROWSER_PATH, path])
        elif os.path.isfile(path):
            subprocess.run([FILEBROWSER_PATH, '/select,', os.path.normpath(path)])
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
    sys.exit()