import sys
sys.path.append("..")

from MainWindow.MainWindow import MainWindow
from PyQt5.QtWidgets import QApplication
from server import ServerSocket
import sys
import time
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from multiprocessing import Process, Queue
import os
import signal
from socket import *


class MainProcessing(MainWindow):
    def __init__(self):
        self.q_GUI_ROS = Queue()
        self.q_GUI_Socket = Queue()
        self.q_ROS_Socket = Queue()
        self.client_connect = False

       
    def StartGUI(self):
        app = QApplication(sys.argv)
        main_window = MainWindow(self.q_GUI_ROS, self.q_GUI_Socket)
        main_window.InitUI()
        sys.exit(app.exec_())

    def StartROSNode(self):
        rospy.init_node('main', anonymous=True)
        vel_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        stated_ROS_node = True
        pid_publisher = rospy.Publisher('/pid', String, queue_size=10)
        GUI_data = []
        data_pub = []
        socket_data = []
        while not rospy.is_shutdown():
            if self.q_ROS_Socket.qsize() != 0:
                socket_data = self.q_ROS_Socket.get()
                self.client_connect = socket_data[0]
            if self.client_connect == False:
                if self.q_GUI_ROS.qsize() != 0:
                    GUI_data = self.q_GUI_ROS.get()
                    data_pub = GUI_data
            else:
                print(self.client_connect)

            RobotControl(data_pub, vel_publisher, pid_publisher)

    def StartSocket(self):
        server_socket = socket(AF_INET, SOCK_STREAM, 0)
        server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        IP = '127.0.0.1'
        PORT = 15555
        server_socket.bind((IP, PORT))
        socket_ros_data = []
        socket_ros_data.append(False)
        self.q_GUI_Socket.put(False)
        self.q_ROS_Socket.put(socket_ros_data)
        server_socket.listen()
        client_fd, client_addr = server_socket.accept()
        socket_ros_data.append(True)
        self.q_GUI_Socket.put(True)
        self.q_ROS_Socket.put(socket_ros_data)
        


def RobotControl(data, vel_pub, pid_pub):
    msg = Twist()
    if len(data) != 0:
        msg.linear.x = int(data[1][0])
        msg.linear.y = int(data[1][1])
        msg.linear.z = int(data[1][2])
        msg.angular.x = int(data[2][0])
        msg.angular.y = int(data[2][1])
        msg.angular.z = int(data[2][2])
        vel_pub.publish(msg)
        pid_pub.publish(str(data[0]))


main_process = MainProcessing()
stated_roscore = False

def StartROSCore():
    global stated_roscore 
    try:
        if stated_roscore == False:
            os.system('roscore')
            stated_roscore = True
    except:
        pass



def main():
    p_0 = Process(target=StartROSCore)

    p_1 = Process(target=main_process.StartGUI)

    p_2 = Process(target=main_process.StartROSNode)

    p_3 = Process(target=main_process.StartSocket)

    p_0.start()
    p_1.start()
    p_2.start()
    p_3.start()

    while p_1.is_alive() == True:
        continue
    my_pid = os.getpid()
    os.system("pkill -P {0}".format(my_pid))


if __name__ == "__main__":
    try:
        main()
    except:
        exit(1)

