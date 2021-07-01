import json

from PySide6.QtCore import QFile, QTextStream
from PySide6.QtWidgets import QMessageBox, QInputDialog, QLineEdit


class Theme:
    def __init__(self, parent):
        self.widget = parent

    def getTheme(self):
        with open('settings.json', 'r') as f:
            settings = json.load(f)
            return settings['theme']

    def applyTheme(self, theme_key):
        """
        @type theme_key: str
        """
        settings = {'theme': theme_key}
        with open('settings.json', 'w') as f:
            json.dump(settings, f)

        self.widget.style().unpolish(self.widget)
        file = QFile(self.widget.theme[theme_key])
        if not file.open(QFile.ReadOnly | QFile.Text):
            raise Exception("FileNotFound")
        style = QTextStream(file)
        self.widget.setStyleSheet(style.readAll())
        self.widget.style().polish(self.widget)
        self.widget.update()


# shows message in the screne with a ok button
def showMessage(widget, title, message):
    """method to show any message to the user with a title and description"""
    msg = QMessageBox()
    msg.about(widget, title, message)


# shows message with a QLineEdit to enter a text
def showDialog(widget, title, message):
    text, ok = QInputDialog.getText(widget, title, message, QLineEdit.Normal)
    if ok:
        return text
    return None


# shows a yes or no question
def askQuestion(widget, title, message):
    buttonReply = QMessageBox.question(widget, title, message, QMessageBox.Yes or QMessageBox.No, QMessageBox.No)
    if buttonReply == QMessageBox.Yes:
        return True
    return False
