from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator
import sys

class Ui_MainWindow(object):
    def __init__(self):
        self.mainWindow = QtWidgets.QMainWindow()
        self.mainWindow.show()
        self.counter=0
        self.numberOfParticipants=0

    def setupUi(self):
        self.step1()

    def step1(self):
        self.mainWindow.setObjectName("mainWindow")
        self.mainWindow.resize(538, 233)

        self.centralwidget = QtWidgets.QWidget(self.mainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.mainLabel = QtWidgets.QLabel(self.centralwidget)
        self.mainLabel.setGeometry(QtCore.QRect(70, 30, 391, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mainLabel.setFont(font)
        self.mainLabel.setObjectName("mainLabel")

        self.numberCombo = QtWidgets.QComboBox(self.centralwidget)
        self.numberCombo.setGeometry(QtCore.QRect(220, 80, 81, 31))
        self.numberCombo.setObjectName("numberCombo")
        self.numberCombo.addItem("4")
        self.numberCombo.addItem("8")
        self.numberCombo.addItem("16")
        self.numberCombo.addItem("32")
        self.numberCombo.addItem("64")
        self.numberCombo.addItem("128")
        self.numberCombo.addItem("256")
        self.numberCombo.addItem("512")

        self.confirmButton = QtWidgets.QPushButton(self.centralwidget)
        self.confirmButton.setGeometry(QtCore.QRect(200, 150, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.confirmButton.setFont(font)
        self.confirmButton.setObjectName("confirmButton")
        self.confirmButton.clicked.connect(lambda: self.step1ConfirmAction(self.numberCombo))

        self.mainWindow.setCentralWidget(self.centralwidget)

        QtCore.QMetaObject.connectSlotsByName(self.mainWindow)

        _translate = QtCore.QCoreApplication.translate
        self.mainWindow.setWindowTitle(_translate("mainWindow", "Sports Scheduler"))
        self.mainLabel.setText(_translate("mainWindow", "Please enter the number of players in the tournament:"))
        self.confirmButton.setText(_translate("mainWindow", "CONFIRM"))

    def step1ConfirmAction(self, comboBox):
        self.step2(int(comboBox.currentText()))

    def step2(self, participants):
        self.numberOfParticipants=participants
        self.mainWindow.setObjectName("mainWindow")
        self.mainWindow.resize(640, 451)
        self.mainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

        self.centralwidget = QtWidgets.QWidget(self.mainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.mainLabel = QtWidgets.QLabel(self.centralwidget)
        self.mainLabel.setGeometry(QtCore.QRect(140, 40, 371, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(26)
        self.mainLabel.setFont(font)
        self.mainLabel.setObjectName("mainLabel")

        self.nameLabel = QtWidgets.QLabel(self.centralwidget)
        self.nameLabel.setGeometry(QtCore.QRect(90, 150, 111, 31))
        self.nameLabel.setObjectName("nameLabel")

        self.nameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.nameInput.setGeometry(QtCore.QRect(250, 150, 321, 31))
        self.nameInput.setObjectName("nameInput")

        self.rollLabel = QtWidgets.QLabel(self.centralwidget)
        self.rollLabel.setGeometry(QtCore.QRect(90, 190, 111, 31))
        self.rollLabel.setObjectName("rollLabel")

        self.rollInput = QtWidgets.QLineEdit(self.centralwidget)
        self.rollInput.setGeometry(QtCore.QRect(250, 190, 91, 31))
        self.rollInput.setObjectName("rollInput")
        self.rollInput.setValidator(QIntValidator(1,90))

        self.streamLabel = QtWidgets.QLabel(self.centralwidget)
        self.streamLabel.setGeometry(QtCore.QRect(90, 230, 111, 31))
        self.streamLabel.setObjectName("streamLabel")

        self.streamCombo = QtWidgets.QComboBox(self.centralwidget)
        self.streamCombo.setGeometry(QtCore.QRect(250, 230, 91, 31))
        self.streamCombo.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.streamCombo.setObjectName("streamCombo")
        self.streamCombo.addItem("BCA")
        self.streamCombo.addItem("BBA")
        self.streamCombo.addItem("BHM")

        self.yearLabel = QtWidgets.QLabel(self.centralwidget)
        self.yearLabel.setGeometry(QtCore.QRect(90, 270, 111, 31))
        self.yearLabel.setObjectName("yearLabel")

        self.yearCombo = QtWidgets.QComboBox(self.centralwidget)
        self.yearCombo.setGeometry(QtCore.QRect(250, 270, 91, 31))
        self.yearCombo.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.yearCombo.setObjectName("yearCombo")
        self.yearCombo.addItem("1st")
        self.yearCombo.addItem("2nd")
        self.yearCombo.addItem("3rd")

        self.confirmButton = QtWidgets.QPushButton(self.centralwidget)
        self.confirmButton.setGeometry(QtCore.QRect(260, 350, 141, 41))
        self.confirmButton.setObjectName("confirmButton")
        self.confirmButton.clicked.connect(self.step2ConfirmAction)

        self.mainWindow.setCentralWidget(self.centralwidget)

        QtCore.QMetaObject.connectSlotsByName(self.mainWindow)

        _translate = QtCore.QCoreApplication.translate
        self.mainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mainLabel.setText(_translate("MainWindow", "Input Participant Details"))
        self.nameLabel.setText(_translate("MainWindow", "ENTER NAME:"))
        self.rollLabel.setText(_translate("MainWindow", "ENTER ROLL NUMBER:"))
        self.confirmButton.setText(_translate("MainWindow", "CONFIRM"))
        self.streamLabel.setText(_translate("MainWindow", "ENTER STREAM"))
        self.yearLabel.setText(_translate("MainWindow", "ENTER YEAR"))

    def step2ConfirmAction(self):
        self.counter+=1
        # print(self.counter, self.numberOfParticipants)
        if(self.counter==self.numberOfParticipants):
            sys.exit()
        else:
            self.step2(self.numberOfParticipants)

if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui=Ui_MainWindow()
    ui.setupUi()
    app.exec_()