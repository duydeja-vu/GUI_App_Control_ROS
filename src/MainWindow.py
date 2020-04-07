from socket import *
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import sys
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        path = os.path.join(os.getcwd())
        print(path)
        self.title = "Robot Control Application"
        self.x = 200
        self.y = 200
        self.width = 500
        self.height = 500
    
    
    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.text_box = QLineEdit(self)
        self.text_box.move(150, 130)
        self.text_box.resize(200, 50)
        self.button = QPushButton("ENTER", self)
        self.button.move(200, 200)
        self.button.clicked.connect(self.OnClick)
        self.show()

    def OnClick(self):
        text_box_value = self.text_box.text()
        return text_box_value

    

    


app = QApplication([])

window = MainWindow()
window.InitUI()



sys.exit(app.exec_())