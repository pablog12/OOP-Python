# Import QApplication and the required widgets from PyQt5.QtWidgets
from PyQt5 import QtWidgets, uic

# Create a subclass of QMainWindow to setup the calculator's GUI
class PyCalcUi(QMainWindow):
    """PyCalc's View (GUI)."""
    def __init__(self):
        """View initializer."""
        super().__init__()
        app = QtWidgets.QApplication(sys.argv)
        window = uic.loadUi("mainwindow.ui")
        window.show()
        app.exec()


    def setDisplayText(self, text):
        """Set display's text."""
        self.display.setText(text)
        self.display.setFocus()

    def displayText(self):
        """Get display's text."""
        return self.display.text()

    def clearDisplay(self):
        """Clear the display."""
        self.setDisplayText('')


        

