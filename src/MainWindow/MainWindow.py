import sys
import os
from multiprocessing import Process
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QAction, QLineEdit, QMessageBox, QTextBrowser
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import os


class MainWindow(QMainWindow):
    def __init__(self, q_GUI_ROS=None, q_Socket_GUI=None, q_GUI_Socket=None, is_server=False, is_client=False):
        super().__init__()
        self.title = "Robot Control Panel"
        self.x = 0
        self.y = 0
        self.width = 800
        self.height = 600
        self.q_GUI_ROS = q_GUI_ROS
        self.q_Socket_GUI = q_Socket_GUI
        self.q_GUI_Socket = q_GUI_Socket
        self.remote_control_mode = False
        self.is_server = is_server
        self.is_client = is_client

    def CreateTextBox(self, text_name, x, y, width, height):
        new_text = QLineEdit(self)
        new_text.setGeometry(x, y, width, height)
        return new_text

    def CreateButton(self, button_name, x, y, width, height):
        new_button = QPushButton("{0}".format(button_name), self)
        new_button.setGeometry(x, y, width, height)
        return new_button

    def CreateLabel(self, label_name, x, y, width, height):
        new_label = QLabel(self)
        new_label.setText("{0}".format(label_name))
        new_label.setGeometry(x, y, width, height)
        return new_label

    def CreateTextBrowser(self, text_browser_name, x, y, width, height):
        text_browser = QTextBrowser(self)
        text_browser.setGeometry(x, y, width, height)
        return text_browser

    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.title_label = self.CreateLabel("CONTROL PANEL", 350, 30, 151, 61)
        self.send_data_label = self.CreateLabel("SEND DATA", 180, 110, 151, 20)
        self.recv_data_label = self.CreateLabel(
            "RECEIVE DATA", 540, 110, 151, 20)
        self.p_label = self.CreateLabel("P", 80, 160, 111, 31)
        self.i_label = self.CreateLabel("I", 80, 200, 111, 31)
        self.d_label = self.CreateLabel("D", 80, 240, 111, 31)
        self.v_label = self.CreateLabel("V", 80, 280, 111, 31)
        self.v_ref_label = self.CreateLabel("V REF", 80, 320, 111, 31)
        self.linear_label = self.CreateLabel(
            "X, Y, Z LINEAR", 80, 360, 111, 31)
        self.angular_label = self.CreateLabel(
            "X, Y, Z ANGULAR", 80, 400, 111, 31)
        self.p_value = self.CreateTextBox("p_value", 230, 160, 113, 25)
        self.i_value = self.CreateTextBox("p_value", 230, 200, 113, 25)
        self.d_value = self.CreateTextBox("p_value", 230, 240, 113, 25)
        self.v_value = self.CreateTextBox("p_value", 230, 280, 113, 25)
        self.v_ref_value = self.CreateTextBox("p_value", 230, 320, 113, 25)
        self.linear_value = self.CreateTextBox("p_value", 230, 360, 113, 25)
        self.angular_value = self.CreateTextBox("p_value", 230, 400, 113, 25)
        self.confirm_button = self.CreateButton("CONFIRM", 160, 450, 89, 25)
        self.confirm_button.clicked.connect(self.ConfirmButtonHandle)
        self.cmd_vel_button = self.CreateButton("/cmd_vel", 550, 160, 89, 25)
        self.cmd_vel_button.clicked.connect(self.CmdVelButtonHandle)
        self.odom_button = self.CreateButton("/odom", 550, 200, 89, 25)
        self.odom_button.clicked.connect(self.OdomButtonHandle)
        self.laser_button = self.CreateButton("/laser_scan", 550, 240, 89, 25)
        self.pid_button = self.CreateButton("/pid", 550, 280, 89, 25)
        self.pid_button.clicked.connect(self.PIDButtonHandle)
        self.text_browser = self.CreateTextBrowser("Name", 460, 330, 256, 192)
        self.show()

    def ConfirmButtonHandle(self):
        self.text_browser.clear()
        data = []

        if self.is_server == True:
            if self.q_Socket_GUI.qsize() != 0:
                self.remote_control_mode = self.q_Socket_GUI.get()

            if self.remote_control_mode == False:
                pid_data = []
                pid_data.append(self.p_value.text())
                pid_data.append(self.i_value.text())
                pid_data.append(self.d_value.text())
                pid_data.append(self.v_value.text())
                pid_data.append(self.v_ref_value.text())
                linear_data = self.linear_value.text().split(',')
                angular_data = self.angular_value.text().split(',')

                if len(linear_data) < 3:
                    for i in range(len(linear_data), 3):
                        linear_data.append(None)

                if len(angular_data) < 3:
                    for i in range(len(angular_data), 3):
                        angular_data.append(None)

                data.append(pid_data)
                data.append(linear_data)
                data.append(angular_data)
                self.SetCommand(data)
                self.q_GUI_ROS.put(data)

            else:
                self.SetCommand("On Remote Control Mode")
                

        if self.is_client == True:
            self.SetCommand("Client")


    def CmdVelButtonHandle(self):
        self.text_browser.clear()
        output = self.linear_value.text() + " " + self.angular_value.text()
        self.SetCommand(output)

    def OdomButtonHandle(self):
        self.text_browser.clear()

    def PIDButtonHandle(self):
        self.text_browser.clear()
        #output = self.linear_value.text() + " " + self.angular_value.text()

    def SetCommand(self, command):
        self.text_browser.setText(str(command))
