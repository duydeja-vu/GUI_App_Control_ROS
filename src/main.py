from MainWindow import MainWindow
from PyQt5.QtWidgets import QApplication
import sys
import time
import asyncio
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from multiprocessing import Process, Queue

q = Queue()

def StartGUI():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.InitUI()
    value = q.get()
    sys.exit(app.exec_())


    

    
    


def main():
    p_1 = Process(target=StartGUI)
    p_1.start()
    rospy.init_node('main', anonymous=True)
    vel_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    pid_publisher = rospy.Publisher('/pid', String, queue_size=10)
    q.put(["Start ROS", 1])
        
    rospy.spin()


if __name__ == "__main__":
    main()
        




