from MainWindow import MainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import *
import sys
import time

SERVER_PORT = 15555
SERVER_IP = ""




app = QApplication([])
    
main_window = MainWindow()
main_window.InitUI()


sys.exit(app.exec_())


