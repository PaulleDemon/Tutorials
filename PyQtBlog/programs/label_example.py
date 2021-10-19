import sys
from PyQt5.QtWidgets import QApplication, QLabel


if __name__ == '__main__':

    app = QApplication(sys.arg)

    label = QLabel("Sample label")
    label.show()

    sys.exit(app.exec())