from http import client
from multiprocessing.connection import wait
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
import sys
import os
import urllib.request
from urllib.request import Request, urlopen
import shutil
import zipfile
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog
from PyQt5.QtGui import *
import PyQt5.QtGui
import re

'''p = re.compile('.[.]..[.].[.].') # 문자 싹 날리면 점 3개 남음 
os.chdir('res_mods')
for i in os.listdir():
    d = p.findall(i)
    if d == []:
        continue
    print(d)
print(d)'''
string = '1.17.1.0'
print(os.listdir())
os.chdir('res_mods')
print(os.listdir())
for i in os.listdir():
    newstring = re.sub(r'[0-9]+', '', string)
    print(newstring)
    if newstring == '...':
        print('walalaru')
        print(i)
        





    