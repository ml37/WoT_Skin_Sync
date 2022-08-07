from mailbox import linesep
from PyQt5.QtWidgets import QPushButton, QWidget, QLabel, QApplication, QMainWindow, QFileDialog, QAction
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
from PyQt5 import uic
import sys
import os
import urllib.request
from urllib.request import Request, urlopen
import shutil
import zipfile
import threading
import re
form_class = uic.loadUiType("SyncTank.ui")[0]

########################################################
DataFolder = 'c:\SyncTank'
########################################################
#Find Data folder. If not found, create it.
if os.path.isdir(DataFolder) == False:
    print('Data folder not found. Creating it.')
    os.mkdir(DataFolder)
########################################################
#Find Data folder/Zipmaker. If not found, create it. Zipmaker is used to create zip files.
if os.path.isdir(DataFolder + '\Zipmaker') == False:
    print('Zipmaker folder not found. Creating it.')
    os.mkdir(DataFolder + '\Zipmaker')
########################################################
#Find Data folder/DLserver.inf. If not found, create it. DLserver.inf is used to store the server information.
if os.path.isfile(DataFolder + '\DLserver.inf') == False:
    with open(DataFolder + '\DLserver.inf', 'w') as f:
        f.write('mashiro37.i234.me') #My server :)
########################################################
#Open DLserver.inf and read the server address.
with open(DataFolder + '\DLserver.inf', 'r') as f:
    DLServer = f.read()
    if DLServer == 'mashiro37.i234.me':
        print('Notice : DLserver set mashiro37.i234.me(Default)')
        DLServer = 'http://' + 'mashiro37.i234.me'
    else:
        print(f'Notice : DLserver set {DLServer}')
        DLServer = 'http://' + DLServer
########################################################
#Open ClientLoaction.inf and read the client location.
if os.path.isfile(DataFolder + '\ClientLocation.inf') == False:
    print(f'ERROR! : {DataFolder}\ClientLocation.inf is not found')
    client_location = 'error'
else: #If ClientLocation.inf is found, read the location.
    with open(DataFolder + '\ClientLocation.inf', 'r') as f:
        client_location = f.readline()
        print(f'Notice : client location : {client_location}')
########################################################
#Open ServerLocation.inf and read the server location.
if os.path.isfile(DataFolder + '\Zipmaker' +'\ServerLocation.inf') == False: #If ServerLocation.inf is not found, set server_location to error.
    print(f'ERROR! : {DataFolder}\Zipmaker\ServerLocation.inf is not found')
    server_location = 'error'
else:
    with open(DataFolder + '\Zipmaker' +'\ServerLocation.inf', 'r') as f: #If ServerLocation.inf is found, read the location.
        server_location = f.readline()
        print(f'Notice : server location : {server_location}')
########################################################
DLSkinlist = DLServer + '/WoTskin/' + 'PySkin/' + 'Skinlist.inf'
DLVersion = DLServer + '/WoTskin/' + 'Version.inf'
DLtemp = client_location + '\\SkinTemp' + '\\PySyncTank\\' + '\\DLtemp\\'
Unziptemp = client_location + '\\SkinTemp' + '\\PySyncTank\\' + '\\Unziptemp\\' 
ZipMaketemp = client_location + '\\SkinTemp' + '\\PySyncTank\\' + '\\ZipMaketemp\\'  
country = {'A':'american', 'GB':'british', 'Ch':'chinese', 'Cz':'czech', 'F':'french', 'G':'german', 'It':'italy', 'J':'japan', 'Pl':'poland', 'R':'russian', 'S':'sweden'}
country_reverse = {'american':'A', 'british':'GB', 'chinese':'Ch', 'czech':'Cz', 'french':'F', 'german':'G', 'italy':'It', 'japan':'J', 'poland':'Pl', 'russian':'R', 'sweden':'S'}
countryimg = {'A':'usa', 'GB':'uk', 'Ch':'china', 'Cz':'czech', 'F':'france', 'G':'germany', 'It':'italy', 'J':'japan', 'Pl':'poland', 'R':'ussr', 'S':'sweden'}
########################################################
#Find SkinList.inf. If Not Exists, Download Skinlist.inf.
if os.path.isfile(DataFolder + '\Skinlist.inf') == False:
    print('c:\SyncTank\Skinlist.inf is not found')
    try:
        urllib.request.urlretrieve(DLSkinlist, DataFolder + '/Skinlist.inf')
    except urllib.error.HTTPError as e:
        print(e.__dict__)
    except urllib.error.URLError as e:
        print(e.__dict__)


########################################################
#Critical Error
if client_location == 'error':
    print('client location is not found') #initialte phaze have a set client location. No need to fix
else:
    if os.path.isdir(client_location + '\SkinTemp') == False:   
        os.mkdir(client_location + '\\SkinTemp')
    if os.path.isdir(client_location + '\SkinTemp' + '\PySyncTank') == False:
        os.mkdir(client_location + '\\SkinTemp\\PySyncTank')
    if os.path.isdir(client_location + '\SkinTemp' + '\PySyncTank' + '\DLtemp') == False:
        os.mkdir(client_location + '\\SkinTemp\\PySyncTank\\DLtemp')
    if os.path.isdir(client_location + '\\SkinTemp' + '\\PySyncTank' + '\\Unziptemp') == False:
        os.mkdir(client_location + '\\SkinTemp\\PySyncTank\\Unziptemp')
    Version = 'error'
    if os.path.isfile(client_location + '\\paths.xml') == False:
        print('Auto Version Detecte Failed')
        ########################################################
        #Find Version.inf. If not found, create it. Version.inf is used to store the version information.
        if os.path.isfile(DataFolder + '\Version.inf') == False:
            print('c:\SyncTank\Version.inf is not found')
            try:
                urllib.request.urlretrieve(DLVersion, DataFolder + '/Version.inf')
            except urllib.error.HTTPError as e:
                print(e.__dict__)
            except urllib.error.URLError as e:
                print(e.__dict__)
        ########################################################
        #Version.inf is read and stored in version.
        Version = 'error' 
        with open(DataFolder + '\Version.inf', 'r') as f:
            Version = f.readline()
            print(f'Notice : Version.inf Read! Version is {Version}')
        if Version == 'error':
            print('Version is not found')
        else:
            if os.path.isdir(client_location + '\\res_mods\\' + Version) == False:
                os.mkdir(client_location + '\\res_mods\\' + Version)
            if os.path.isdir(client_location + '\\res_mods\\' + Version + '\\vehicles') == False:
                os.mkdir(client_location + '\\res_mods\\' + Version + '\\vehicles')
    else:
        r = open(client_location + '\\paths.xml', 'r')
        for line in r:
            if '/res_mods/' in line:
                '''    <Path cacheSubdirs="true">./res_mods/1.17.1.0</Path>'''
                Version = line.split('/res_mods/')[1].split('</Path>')[0]
                print(f'Notice : Version is {Version} by reading paths.xml')
                break
        r.close()


class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('SyncTank')
        self.setWindowIcon(QIcon('icon.ico'))
        self.setAcceptDrops(True)
        self.load_skin_list()
        self.setBaseSize(800, 560)
        ########################################################
        #connect
        self.listWidget.itemClicked.connect(self.on_item_clicked)
        self.btn_download.clicked.connect(self.download)
        self.btn_opencl.clicked.connect(self.opencl)
        self.btn_openus.clicked.connect(self.openus)
        self.btn_manuallist.clicked.connect(self.manuallist)
        self.btn_all.clicked.connect(self.all)
        self.btn_cleartemp.clicked.connect(self.cleartemp)
        self.btn_reload.clicked.connect(self.load_skin_list)
        self.btn_open_skin.clicked.connect(self.open_skin)
        self.btn_opentemp.clicked.connect(self.opentemp)
        self.cb_country.currentIndexChanged.connect(self.country_change)
        self.btn_change_DLserver.clicked.connect(self.change_DLserver)
        self.btn_go.clicked.connect(self.search_list)
        ########################################################
        #setEnabled
        self.btn_open_skin.setEnabled(False)
        self.btn_download.setEnabled(False)
        self.btn_openus.setEnabled(False)
        self.btn_manuallist.setEnabled(False)
        ########################################################
        selClientLoc = QAction('Select Game Client Location', self)
        selClientLoc.triggered.connect(self.selClientLocation)
        selServerLoc = QAction('Select Upload Server Location(Option for Server Admin, Not For User!!)', self)
        selServerLoc.triggered.connect(self.selServerLocation)
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('&Load')
        fileMenu.addAction(selClientLoc)
        fileMenu.addAction(selServerLoc)
        ########################################################
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
            self.lbl_serverlocation.setText('Server Location : ' + fname + 'To use this options, please restart the program')
            self.btn_openus.setVisible(True)
            self.btn_manuallist.setVisible(True)
    def manuallist(self):
        path = server_location
        file_list = os.listdir(path)
        file_list_zip = [file for file in file_list if file.endswith(".zip")]
        f = open(server_location + '\Skinlist.inf', 'w')
        for file in file_list_zip:
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
    def opentemp(self):
        print('opentemp')
        if os.path.isdir(client_location + '\\SkinTemp' + '\\PySyncTank' + '\\DLtemp') == True:
            os.startfile(client_location + '\\SkinTemp' + '\\PySyncTank' + '\\DLtemp')
        if os.path.isdir(client_location + '\\SkinTemp' + '\\PySyncTank' + '\\Unziptemp') == True:
            os.startfile(client_location + '\\SkinTemp' + '\\PySyncTank' + '\\Unziptemp')
    def country_change(self):
        def load_flag_from_web():
                url_flag = 'http://tanks.gg/img/nations/' + countryimg[country_reverse[self.cb_country.currentText()]] + '.svg'
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
                self.qPixmapWebVar_flag = self.qPixmapWebVar_flag.scaledToWidth(60)
                self.lbl_img_2.setPixmap(self.qPixmapWebVar_flag)
                self.lbl_img_2.setHidden(False)
        if self.cb_country.currentText() == 'All':
            self.load_skin_list()
        else:
            print(f'country_change {self.cb_country.currentText()}')
            self.listWidget.clear()
            try:
                urllib.request.urlretrieve(DLSkinlist, DataFolder + '/Skinlist.inf')
            except urllib.error.HTTPError as e:
                print(e.__dict__)
                self.btn_download.setEnabled(False)
                self.lbl_error.setText('Error!')
                self.lbl_error_2.setText(str(e.reason))
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
                string = text[0]
                newstring = re.sub(r'[0-9]+', '', string)
                if newstring == country_reverse[self.cb_country.currentText()]:
                    self.listWidget.addItem(i)
            f.close()
            self.label.setText('Total ' + skin_count + ' Skins, ' + self.cb_country.currentText() + ' listed ' + str(self.listWidget.count()) + ' Skins')
            t1 = threading.Thread(target=load_flag_from_web)
            t1.start()
            
        
    def load_skin_list(self):
        self.listWidget.clear()
        try:
            urllib.request.urlretrieve(DLSkinlist, DataFolder + '/Skinlist.inf')
        except urllib.error.HTTPError as e:
            print(e.__dict__)
            self.btn_download.setEnabled(False)
            self.lbl_error.setText('Error!')
            self.lbl_error_2.setText(str(e.reason))
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
            global skin_count
            skin_count = str(self.listWidget.count())
            self.label.setText('Total ' + skin_count + ' Skins')
        f.close()
        self.lbl_Version.setText('Version : ' + Version)
        self.lbl_clientlocation.setText('Client Location : ' + client_location)
        self.lbl_serverlocation.setText('Server Location : ' + server_location)
        if server_location == 'error':
            self.lbl_serverlocation.setText('')
            self.btn_openus.setVisible(False)
            self.btn_manuallist.setVisible(False)
        self.lbl_DLserver.setText('DL Server : ' + DLServer)

    def on_item_clicked(self, item):
        self.btn_open_skin.setEnabled(True)
        self.btn_download.setEnabled(True)
        self.lbl_img.setHidden(True)
        self.lbl_img_2.setHidden(True)
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
        def load_img_from_web():
                url = 'http://tanks.gg/img/tanks/' + countryimg[vehicle_Countrycode] + '-' + lawname + '.png'
                try:
                    image=Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                except urllib.error.HTTPError as e:
                    print(e.__dict__)
                    self.btn_download.setEnabled(False)
                    self.lbl_error.setText('Error!')
                    self.lbl_error_2.setText(str(e.reason))
                    self.lbl_img.setText('Error!')
                except urllib.error.URLError as e:
                    print(e.__dict__)
                    self.btn_download.setEnabled(False)
                    self.lbl_error.setText('Error!')
                    self.lbl_error_2.setText(str(e.reason))
                    self.lbl_img.setText('Error!')
                image_data = urlopen(image).read()
                self.qPixmapWebVar = QPixmap()
                self.qPixmapWebVar.loadFromData(image_data)
                self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(320) # 480x300 320x200 360x240 
                self.lbl_img.setPixmap(self.qPixmapWebVar)
                self.lbl_img.setHidden(False)
        def load_flag_from_web():
                url_flag = 'http://tanks.gg/img/nations/' + countryimg[vehicle_Countrycode] + '.svg'
                try:
                    image_flag = Request(url_flag, headers={'User-Agent': 'Mozilla/5.0'})
                except urllib.error.HTTPError as e:
                    print(e.__dict__)
                    self.btn_download.setEnabled(False)
                    self.lbl_error.setText('Error!')
                    self.lbl_error_2.setText(str(e.reason))
                    self.lbl_img.setText('Error!')
                except urllib.error.URLError as e:
                    print(e.__dict__)
                    self.btn_download.setEnabled(False)
                    self.lbl_error.setText('Error!')
                    self.lbl_error_2.setText(str(e.reason))
                    self.lbl_img.setText('Error!')
                image_data_flag = urlopen(image_flag).read()
                self.qPixmapWebVar_flag = QPixmap()
                self.qPixmapWebVar_flag.loadFromData(image_data_flag)
                self.qPixmapWebVar_flag = self.qPixmapWebVar_flag.scaledToWidth(60)
                self.lbl_img_2.setPixmap(self.qPixmapWebVar_flag)
                self.lbl_img_2.setHidden(False)
        t = threading.Thread(target=load_img_from_web)
        t.start()
        t1 = threading.Thread(target=load_flag_from_web)
        t1.start()
    def search_list(self):
        if self.search.text() == '':
            print('ERROR! : Searchbar empty')
        elif self.search.text() == ' ':
            print('ERROR! : Searchbar empty')
        else:
            self.country_change()
            out = self.listWidget.findItems(self.search.text(), Qt.MatchContains)
            if out == []:
                '''self.lbl_error.setText('Error!')
                self.lbl_error_2.setText('No Skin Found')'''
                self.label.setText('Total ' + skin_count + ' Skins, ' + 'Not Found')
            else:
                
                '''self.listWidget.clear()
                print('@')
                print(out)'''
                result = []
                for i in out:
                    #print(i.text())
                    result.append(i.text())
                self.listWidget.clear()
                for i in result:
                    self.listWidget.addItem(i)
                #print(result)
                #print(str(self.listWidget.count()))
                self.label.setText('Total ' + skin_count + ' Skins, ' + str(self.listWidget.count()) + ' Found')

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
    def open_skin(self):
        if os.path.isdir(client_location + '/res_mods/' + Version + '/vehicles/' + vehicle_country) == True:
            if os.path.isdir(client_location + '/res_mods/' + Version + '/vehicles/' + vehicle_country + '/' + lawname) == True:
                os.startfile(client_location + '/res_mods/' + Version + '/vehicles/' + vehicle_country + '/' + lawname)
            else:
                print('Folder not found')
        else:
            print('Folder not found')
        '''path = client_location + '/res_mods/' + Version + '/vehicles/' + vehicle_country + '/' + self.listWidget.currentItem().text().replace('/', '\\')
        path = os.path.normpath(path)'''
        '''if os.path.isdir(path):
            subprocess.run([FILEBROWSER_PATH, path])
        elif os.path.isfile(path):
            subprocess.run([FILEBROWSER_PATH, '/select,', os.path.normpath(path)])'''
    def opencl(self):
            # explorer would choke on forward slashes
        path = client_location.replace('/', '\\')
        path = os.path.normpath(path)
        if os.path.isdir(path):
            os.startfile(path)
        '''if os.path.isdir(path):
            subprocess.run([FILEBROWSER_PATH, path])
        elif os.path.isfile(path):
            subprocess.run([FILEBROWSER_PATH, '/select,', os.path.normpath(path)])'''
    def openus(self):
            # explorer would choke on forward slashes
        path = server_location.replace('/', '\\')
        path = os.path.normpath(path)
        if os.path.isdir(path):
            os.startfile(path)
        '''if os.path.isdir(path):
            subprocess.run([FILEBROWSER_PATH, path])
        elif os.path.isfile(path):
            subprocess.run([FILEBROWSER_PATH, '/select,', os.path.normpath(path)])'''
    def change_DLserver(self):
        path = DataFolder.replace('/', '\\')
        path = os.path.normpath(path)
        if os.path.isdir(path):
            os.startfile(path)
        self.listWidget.clear()
        self.load_skin_list()
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
    sys.exit()