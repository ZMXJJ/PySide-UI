import sys

from PyQt5.QtWidgets import QApplication
from ui import MySiliconApp
from PyQt5 import QtCore, QtGui

import siui

siui.gui.set_scale_factor(1)

QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
QtGui.QGuiApplication.setAttribute(QtCore.Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MySiliconApp()
    window.show()
    sys.exit(app.exec_())
