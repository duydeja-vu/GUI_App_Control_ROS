# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designe.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):

    def __init__(self):
        pass

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("Robot Control App")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 400, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.publish = QtWidgets.QLabel(self.centralwidget)
        self.publish.setGeometry(QtCore.QRect(60, 10, 111, 51))
        self.publish.setObjectName("publish")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 400, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(440, 10, 111, 51))
        self.label_2.setObjectName("label_2")
        self.p_key = QtWidgets.QLabel(self.centralwidget)
        self.p_key.setGeometry(QtCore.QRect(20, 70, 67, 17))
        self.p_key.setObjectName("p_key")
        self.i_key = QtWidgets.QLabel(self.centralwidget)
        self.i_key.setGeometry(QtCore.QRect(20, 110, 67, 17))
        self.i_key.setObjectName("i_key")
        self.d_key = QtWidgets.QLabel(self.centralwidget)
        self.d_key.setGeometry(QtCore.QRect(20, 150, 67, 17))
        self.d_key.setObjectName("d_key")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(530, 70, 67, 17))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(390, 70, 67, 17))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(390, 150, 67, 17))
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(390, 110, 67, 17))
        self.label_12.setObjectName("label_12")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(530, 110, 67, 17))
        self.label_14.setObjectName("label_14")
        self.v_key = QtWidgets.QLabel(self.centralwidget)
        self.v_key.setGeometry(QtCore.QRect(20, 190, 67, 17))
        self.v_key.setObjectName("v_key")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(60, 360, 89, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(450, 360, 89, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        self.v_ref_key = QtWidgets.QLabel(self.centralwidget)
        self.v_ref_key.setGeometry(QtCore.QRect(20, 220, 91, 31))
        self.v_ref_key.setObjectName("v_ref_key")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(160, 70, 67, 17))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(160, 110, 67, 17))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(160, 150, 67, 17))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(160, 190, 67, 17))
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_5.setGeometry(QtCore.QRect(160, 230, 67, 17))
        self.textEdit_5.setObjectName("textEdit_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 628, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Robot Control"))
        MainWindow.setGeometry(0, 0, 1800, 960)
        self.pushButton.setText(_translate("MainWindow", "Confirm"))
        self.publish.setText(_translate("MainWindow", "   Publish Node"))
        self.pushButton_2.setText(_translate("MainWindow", "Confirm"))
        self.label_2.setText(_translate("MainWindow", "Subcrible Node"))
        self.p_key.setText(_translate("MainWindow", "p"))
        self.i_key.setText(_translate("MainWindow", "i"))
        self.d_key.setText(_translate("MainWindow", "d"))
        self.label_9.setText(_translate("MainWindow", "Value"))
        self.label_10.setText(_translate("MainWindow", "/cmd_vel"))
        self.label_12.setText(_translate("MainWindow", "/odom"))
        self.label_14.setText(_translate("MainWindow", "Value"))
        self.v_key.setText(_translate("MainWindow", "velocity"))
        self.pushButton_3.setText(_translate("MainWindow", "Add Node"))
        self.pushButton_4.setText(_translate("MainWindow", "Add Node"))
        self.v_ref_key.setText(_translate("MainWindow", "velocity ref"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

