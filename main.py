"""
This is the runner file of the application
Mainwindow is created and other widgets are added in this file
"""
import sys
from PySide6.QtWidgets import QApplication
from widgets import UISuperMarket

# runner
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = UISuperMarket()
    window.showMaximized()
    window.show()
    app.exec()
