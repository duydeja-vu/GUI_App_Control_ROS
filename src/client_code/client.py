import socket
from multiprocessing import Process, Queue
import sys

class Client(object):
    def __init__(self):
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        except socket.error as err:
            print("Failed {0}".format(err))
            sys.exit()
    
        self.SERVER_HOST = ''
        self.SERVER_PORT = ''
    
    def ConnectToServer(self):
        self.client_socket.connect((self.SERVER_HOST, self.SERVER_PORT))
        
