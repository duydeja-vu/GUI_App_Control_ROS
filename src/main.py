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



def RobotControl(data):
    msg = Twist()


    vel_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    pid_publisher = rospy.Publisher('/pid', String, queue_size=10)
    if len(data) != 0:
        msg.linear.x = int(data[5][0])
        msg.linear.y = int(data[5][1])
        msg.linear.z = int(data[5][2])
        msg.angular.x = int(data[6][0])
        msg.angular.y = int(data[6][1])
        msg.angular.z = int(data[6][2])
        
        

        

def StartGUI():
    app = QApplication(sys.argv)
    main_window = MainWindow(q)
    main_window.InitUI()
    sys.exit(app.exec_())
   

def StartROS():
    rospy.init_node('main', anonymous=True)
    data = []
    data_temp = []
    while not rospy.is_shutdown():
        if q.qsize() != 0:
            data = q.get()
            data_temp = data
        RobotControl(data_temp)


def main():
    p_1 = Process(target=StartGUI)
    p_2 = Process(target=StartROS)
    p_1.start()
    p_2.start()

   



    
        
    
    
    


    
    
        


if __name__ == "__main__":
    try:
        main()
    except:
        exit(1)
    
        




