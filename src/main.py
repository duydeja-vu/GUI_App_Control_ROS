from MainWindow import MainWindow
from PyQt5.QtWidgets import QApplication
import sys
import time






if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.InitUI()
    main_window.test()
    sys.exit(app.exec_())



