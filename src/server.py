from socket import *
from MainWindow import MainWindow
from PyQt5 import QApplication

class ServerSocket(object):
    def __init__(self, IP, PORT):
        self.IP = IP
        self.PORT = PORT
        self.fd = -1

    def CreateSocket(self):
        self.fd = socket(AF_INET, SOCK_STREAM, 0)
        self.fd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        return self.fd

    def BindAddr(self):
        ADDR = (self.IP, self.PORT)
        self.fd.bind(ADDR)

    def ListenConnection(self, number_client):
        self.fd.listen(number_client)

    def AcceptConnection(self):
        (client_fd, client_addr) = self.fd.accept()
        return (client_fd, client_addr)

    


    







app = QApplication([])

window = MainWindow()
window.InitUI()



sys.exit(app.exec_())