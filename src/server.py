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
        try:
            self.fd.bind(ADDR)
            return True
        except:
            return False

    def ListenConnection(self):
        
        self.fd.listen(5)
        client_fd, client_addr = self.fd.accept()
        return [client_fd, client_addr]
        

    def AcceptConnection(self):
        client_fd, client_addr = self.fd.accept()
        return (client_fd, client_addr)

    def CloseSocket(self):
        self.fd.close()

