import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton


if __name__ == '__main__':

    app = QApplication(sys.argv)

    widget = QWidget()

    label = QLabel("Sample label", parent=widget)
    label.move(50, 50)  # place the button at x=50, y=50 from the top left corner of the application

    button = QPushButton("Button", parent=widget) # create an instance of QPushbutton
    button.move(50, 100)
    
    widget.show()

    sys.exit(app.exec())