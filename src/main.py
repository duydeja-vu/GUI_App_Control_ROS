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

q = Queue()





def StartGUI():
    app = QApplication(sys.argv)
    main_window = MainWindow(q)
    main_window.InitUI()
    sys.exit(app.exec_())
   

def StartROS():
    rospy.init_node('main', anonymous=True)
    data = []
    while True:
        if q.qsize() != 0:
            data = q.get()
        RobotControl(data)


def main():
    p_1 = Process(target=StartGUI)
    p_2 = Process(target=StartROS)
    p_1.start()
    p_2.start()

   



    
        
    
    
    

def RobotControl(data):
    # msg = Twist()
    # vel_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    # pid_publisher = rospy.Publisher('/pid', String, queue_size=10)
    print("Robot control")

    
    
        


if __name__ == "__main__":
    main()
    
        




