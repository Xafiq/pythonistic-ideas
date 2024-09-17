from PySide2 import QtWidgets, QtGui, QtCore

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("currency converter")
        self.setup_ui()

    def setup_ui(self):
        self.layout = QtWidgets.QHBoxLayout(self)
        self.cbb_currencyFrom = QtWidgets.QComboBox()
        self.amount = QtWidgets.QSpinBox()
        self.cbb_currencyTo = QtWidgets.QComboBox()
        self.le_ConvertedAmount = QtWidgets.QSpinBox()
        self.btn_reverse = QtWidgets.QPushButton("Reverse currencies")

        self.layout.addWidget(self.cbb_currencyFrom)
        self.layout.addWidget(self.amount)
        self.layout.addWidget(self.cbb_currencyTo)
        self.layout.addWidget(self.ConvertedAmount)
        self.layout.addWidget(self.btn_reverse)
  
app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec_()
