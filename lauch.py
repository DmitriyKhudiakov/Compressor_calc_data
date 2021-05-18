import sys
from PyQt5.QtWidgets import QApplication
from classes.MainWidget import MainWidget


def start():
    app = QApplication(sys.argv)
    win = MainWidget()
    sys.exit(app.exec_())
