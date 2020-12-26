#!/usr/bin/env python3

# Filename: pycalc.py

"""PyCalc is a simple calculator built using Python and PyQt5."""

import sys
from PyQt5.QtWidgets import QApplication

# MVC
from model import evaluateExpression, ERROR_MSG
from view import PyCalcUi
from controller import PyCalcCtrl

__version__ = '0.1'
__author__ = 'Leodanis Pozo Ramos'

# Client code
def main():
    """Main function."""
    # Create an instance of QApplication
    pycalc = QApplication(sys.argv)
    # Show the calculator's GUI
    view = PyCalcUi()
    view.show()
    # Create instances of the model and the controller
    model = evaluateExpression
    PyCalcCtrl(model=model, view=view)
    # Execute the calculator's main loop
    sys.exit(pycalc.exec_())

if __name__ == '__main__':
    main()