from PySide6.QtWidgets import QMessageBox, QInputDialog, QLineEdit


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
