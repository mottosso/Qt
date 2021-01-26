"""Map all bindings to PySide

This module is a backward compatible for of Qt.py

Resolution order:
    - PySide2
    - PyQt5
    - PySide
    - PyQt4

Usage:
    >>> import sys
    >>> from QtLegacy import QtGui
    >>> app = QtGui.QApplication(sys.argv)
    >>> button = QtGui.QPushButton("Hello World")
    >>> button.show()
    >>> app.exec_()

"""

import sys

__version__ = "0.3.3"

import Qt

for key, value in vars(Qt.QtWidgets).iteritems():
    setattr(Qt.QtGui, key, value)

del QtWidgets
sys.modules[__name__] = Qt