import mainui
from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
ui = mainui.Ui_MainWindow()
ui.setupUi()
ui.mainWindow.show()
app.exec_()

sys.exit()