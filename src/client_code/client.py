import socket
from multiprocessing import Process, Queue
import sys

class ClientSocket(object):
    def __init__(self):
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        except socket.error as err:
            print("Failed {0}".format(err))
            sys.exit()
    
        self.SERVER_HOST = '127.0.0.1'
        self.SERVER_PORT = 15555
        self.BUFFSIZE = 1024
    
    def ConnectToServer(self):
        self.client_socket.connect((self.SERVER_HOST, self.SERVER_PORT))
    
    def SendData(self, send_data):
        self.client_socket.send(send_data.encode('utf-8'))

    def RecvData(self):
        recv_data = self.client_socket.recv(self.BUFFSIZE)
        return recv_data







        


