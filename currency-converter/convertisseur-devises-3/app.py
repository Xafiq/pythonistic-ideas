from PySide2 import QtWidgets, QtGui, QtCore
import currency_converter

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.c = currency_converter.CurrencyConverter()
        self.setWindowTitle("Currency Converter")
        self.setup_ui()
        self.set_default_values()

    def setup_ui(self):
        self.layout = QtWidgets.QHBoxLayout(self)
        self.cbb_devisesFrom = QtWidgets.QComboBox()  # ComboBox for the source currency
        self.le_montant = QtWidgets.QSpinBox()  # SpinBox for the amount to convert
        self.cbb_devisesTo = QtWidgets.QComboBox()  # ComboBox for the target currency
        self.le_montantConverti = QtWidgets.QSpinBox()  # SpinBox for the converted amount
        self.btn_inverser = QtWidgets.QPushButton("Swap currencies")  # Button to swap currencies

        self.layout.addWidget(self.cbb_devisesFrom)
        self.layout.addWidget(self.le_montant)
        self.layout.addWidget(self.cbb_devisesTo)
        self.layout.addWidget(self.le_montantConverti)
        self.layout.addWidget(self.btn_inverser)
    
    def set_default_values(self):
        self.cbb_devisesFrom.addItems(sorted(list(self.c.currencies)))  # Populate ComboBox with available currencies
        self.cbb_devisesTo.addItems(sorted(list(self.c.currencies)))  # Populate ComboBox with available currencies
        self.cbb_devisesFrom.setCurrentText("EUR")  # Set default currency to EUR
        self.cbb_devisesTo.setCurrentText("EUR")  # Set default currency to EUR
        self.le_montant.setValue(100)  # Default amount to convert is 100
        self.le_montantConverti.setValue(100)  # Default converted amount is 100
        self.le_montant.setRange(1, 1000000)  # Set the valid range for the amount to convert
        self.le_montantConverti.setRange(1, 1000000)  # Set the valid range for the converted amount

 
app = QtWidgets.QApplication([])  # Initialize the application
win = App()  # Create the app window
win.show()  # Show the window
app.exec_()  # Run the application event loop
