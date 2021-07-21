"""
This is the runner file of the application
It creates the login widget
"""
import sys
from PySide6.QtWidgets import QApplication

from widgets import LoginWidget


# runner
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = LoginWidget()
    window.show()
    app.exec()
