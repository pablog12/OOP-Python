# File: qt-ui.py
import sys, os
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile, QIODevice

class Main(QApplication):
    """PyCalc's View (GUI)."""
    def __init__(self):
        """View initializer."""
        super().__init__()

    def _connectSignals(self):
        """Connect signals and slots."""
        self._view.buttons['triggerButton'].clicked.connect(self._message)

    def _message(self):
        print("You clicked the button!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui_file_name = "form.ui"
    path = os.path.join(os.path.dirname(__file__), ui_file_name)
    ui_file = QFile(path)
    if not ui_file.open(QIODevice.ReadOnly):
        print("Cannot open {}: {}".format(ui_file_name, ui_file.errorString()))
        sys.exit(-1)
    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()
    if not window:
        print(loader.errorString())
        sys.exit(-1)
    window.show()

    sys.exit(app.exec_())

    Main(window)
