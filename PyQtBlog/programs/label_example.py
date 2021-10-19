import sys
from PyQt5 import QtWidgets


if __name__ == '__main__':

    app = QtWidgets.QApplication([])

    win = QtWidgets.QWidget()
    win.setLayout(QtWidgets.QVBoxLayout())
    win.layout().addWidget(QtWidgets.QLabel("Sample label"))

    win.show()

    sys.exit(app.exec())