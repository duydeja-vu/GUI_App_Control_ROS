from MainWindow import MainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import *
import sys
import time






app = QApplication([])
    
main_window = MainWindow()
main_window.InitUI()


sys.exit(app.exec_())


