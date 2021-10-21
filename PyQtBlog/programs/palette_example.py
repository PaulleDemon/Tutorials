import sys
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtGui import  QFont, QPalette, QColor


if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    label = QLabel("hello")
    widget_palette = QPalette()
    widget_palette.setColor(QPalette.Window, QColor("red"))
    widget_palette.setColor(QPalette.WindowText, QColor("#00ff00"))
    label.setFont(QFont("Times new roman", 20))

    label.setPalette(widget_palette)

    label.show()

    sys.exit(app.exec())