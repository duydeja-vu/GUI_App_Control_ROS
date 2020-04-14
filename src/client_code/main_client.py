from MainWindow import MainWindow
from PyQt5.QtWidgets import QApplication
from client import ClientSocket
import sys
import time
from multiprocessing import Process, Queue
import os

class MainProcessing(MainWindow, ClientSocket):
    def __init__(self):
        self.q_GUI_Socket = Queue()
    
    def StartGUI(self):
        app = QApplication(sys.argv)
        main_window = MainWindow(self.q_GUI_Socket)
        main_window.InitUI()
        sys.exit(app.exec_())

    def StartSocket(self):
        client_socket = ClientSocket()
        client_socket.ConnectToServer()

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

