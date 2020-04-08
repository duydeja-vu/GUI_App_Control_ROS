from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from server import ServerSocket
import sys
import os
from multiprocessing import Process


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
        # self.text_box = QLineEdit(self)
        # self.text_box.move(150, 130)
        # self.text_box.resize(200, 50)
        self.button = QPushButton("ENTER for Start Server", self)
        self.button.resize(250, 50)
        self.button.move(140, 130)
        self.button.clicked.connect(self.StartServer)
        self.show()

    def StartServer(self):
        error_message = QLabel(self)
        error_message.resize(250, 50)
        error_message.setText("Server Waiting Client...")
        error_message.move(200, 180)
        error_message.show()
        listen_process = Process(target=self.SocketHandle)
        listen_process.start()
        
        
        
    def SocketHandle(self):
        server_socket = ServerSocket()
        server_socket.IP = '127.0.0.1'
        server_socket.PORT = 15555
        server_socket.BindAddr()
        sum = server_socket.ListenConnection()
        print(sum)
        


        


    
        
        

    
    
    
    


        