from MainWindow import MainWindow
from PyQt5.QtWidgets import QApplication
import sys
import time
import asyncio
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from multiprocessing import Process, Queue
import os


class MainProcessing(MainWindow):
    def __init__(self):
        self.q = Queue()
        self.GUI_process_done = None
        self.ROS_process_done = None

    def StartGUI(self):
        app = QApplication(sys.argv)
        main_window = MainWindow(self.q)
        main_window.InitUI()
        sys.exit(app.exec_())

    def StartROS(self):
        rospy.init_node('main', anonymous=True)
        data = []
        data_temp = []
        while not rospy.is_shutdown():
            if self.q.qsize() != 0:
                data = self.q.get()
                data_temp = data
                #print(self.GUI_process_done)
            RobotControl(data_temp)
            



def RobotControl(data):
    msg = Twist()
    vel_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    pid_publisher = rospy.Publisher('/pid', String, queue_size=10)
    if len(data) != 0:
        msg.linear.x = data[5][0]
        msg.linear.y = data[5][1]
        msg.linear.z = data[5][2]
        msg.angular.x = data[6][0]
        msg.angular.y = data[6][1]
        msg.angular.z = data[6][2]
        print(msg)
        vel_publisher.publish(msg)


main_process = MainProcessing()

def main():
    p_1 = Process(target=main_process.StartGUI)
    p_2 = Process(target=main_process.StartROS)
    p_1.start()
    p_2.start()


if __name__ == "__main__":
    try:
        main()
    except:
        exit(1)
    
        




