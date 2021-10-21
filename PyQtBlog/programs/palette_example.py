import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import  QPalette, QColor


if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    widget = QWidget()
    widget_palette = QPalette()
    widget_palette.setColor(QPalette.Window, QColor("red"))

    widget.setPalette(widget_palette)

    widget.show()

    sys.exit(app.exec())