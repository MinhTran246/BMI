from PyQt6.QtWidgets import QApplication, QMainWindow

from MainwindowExt import MainwindowExt

app=QApplication([])
mainwindow=QMainWindow()
myui=MainwindowExt()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()