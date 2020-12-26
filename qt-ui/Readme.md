# QT UI
Qt Designer uses XML .ui files to store your GUI designs. 

You can load them with QUiLoader. PyQt includes a module called uic to help with this. 
You can also convert the .ui file content into Python code with a command-line tool called pyuic5.


# Licensing
The key difference in the two versions — in fact the entire reason PySide2 exists — is licensing. PyQt5 is available under a GPL or commercial license, and PySide2 under a LGPL license.

If you are planning to release your software itself under the GPL, or you are developing software which will not be distributed, the GPL requirement of PyQt5 is unlikely to be an issue. However, if you plan to distribute your software without distributing the source you will either need to purchase a commercial license from Riverbank for PyQt5 or use PySide2.

The LGPL license does not require you to share the source code of your own applications, even if they are bundled with PySide2. You only need to ensure that the source code covered by the LGPL is made available, including modifications you have made to it, if any. In normal use there will not be any modifications and the standard distributions of PySide2/Qt5 source code will already cover this for you.

`https://www.learnpyqt.com/tutorials/pyqt5-vs-pyside2/`


# Load the .ui file directly
```
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
```

# Conver .ui to code using pyside-uic
`brew install pyside-tools`


## First run the shell with the pyside6 package installed
`pipenv shell`
## Convert the .ui file to a .py
`pyside6-uic form.ui > ui_form.py`
## Import it
`from ui_mainwindow import Ui_MainWindow`


## Example code
```
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
```