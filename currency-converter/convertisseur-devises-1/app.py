from PySide2 import QtWidgets, QtGui, QtCore

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("currency converter")

app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec_()
