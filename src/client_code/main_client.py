import sys
sys.path.append("..")

from MainWindow.MainWindow import MainWindow
from PyQt5.QtWidgets import QApplication
import time
from multiprocessing import Process, Queue
import os
from socket import *

class MainProcessing(MainWindow):
    def __init__(self):
        self.q_GUI_Socket = Queue()
    
    def StartGUI(self):
        app = QApplication(sys.argv)
        main_window = MainWindow(q_GUI_Socket=self.q_GUI_Socket, is_client=True)
        main_window.InitUI()
        sys.exit(app.exec_())

    def StartSocket(self):
        client_socket = socket(AF_INET, SOCK_STREAM, 0)
        SERVER_HOST = '127.0.0.1'
        SERVER_PORT = 15555
        client_socket.connect((SERVER_HOST, SERVER_PORT))
        


main_process = MainProcessing()

def main():
    p_0 = Process(target=main_process.StartGUI)

    p_1 = Process(target=main_process.StartSocket)

    p_0.start()
    p_1.start()

    while p_0.is_alive() == True:
        continue
    my_pid = os.getpid()
    os.system("pkill -P {0}".format(my_pid))

if __name__ == "__main__":
    try:
        main()
    except:
        exit(1)

