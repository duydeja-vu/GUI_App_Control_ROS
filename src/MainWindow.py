from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from server import ServerSocket
import sys
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Robot Control Application"
        self.x = 200
        self.y = 200
        self.width = 500
        self.height = 500
        self.text_box_value = None
    
    
    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.text_box = QLineEdit(self)
        self.text_box.move(150, 130)
        self.text_box.resize(200, 50)
        self.button = QPushButton("ENTER", self)
        self.button.move(200, 200)
        self.button.clicked.connect(self.StartServer)
        self.show()

    def StartServer(self):
        PORT = 15553
        try:
            server_socket = ServerSocket()
            print("Success Create Socket")
        except:
            exit(-1)
        server_socket.IP = self.text_box.text()
        server_socket.PORT = PORT
        server_socket.BindAddr()
        server_socket.ListenConnection(5)
        server_socket.AcceptConnection()
        
        

    
    
    
    


        