import sys
from PyQt5 import QtWidgets
from mainwidget import MainWindow


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    
    with open('theme.qss', 'r') as f_obj:
        theme = f_obj.read()
    
    win = MainWindow()
    win.show() # show the window

    win.setStyleSheet(theme)
    sys.exit(app.exec())