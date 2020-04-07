from socket import *

class ServerSocket(object):
    def __init__(self):
        self.IP = ""
        self.PORT = ""
        self.fd = -1
        self.CreateSocket()

    def CreateSocket(self):
        self.fd = socket(AF_INET, SOCK_STREAM, 0)
        self.fd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    def BindAddr(self):
        ADDR = (self.IP, self.PORT)
        self.fd.bind(ADDR)

    def ListenConnection(self, number_client):
        self.fd.listen(number_client)

    def AcceptConnection(self):
        (client_fd, client_addr) = self.fd.accept()
        return (client_fd, client_addr)