import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout


if __name__ == '__main__':

    app = QApplication(sys.argv)

    widget = QWidget()

    v_layout = QVBoxLayout()

    label = QLabel("Sample label")
    button = QPushButton("Button") # create an instance of QPushbutton
    
    v_layout.addWidget(label)
    v_layout.addWidget(button)

    widget.setLayout(v_layout)

    widget.show()

    sys.exit(app.exec())