import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

def change_button_text():
    button.setText("Button has been clicked")


if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    widget = QWidget()

    v_layout = QVBoxLayout()

    label = QLabel("Sample label")

    button = QPushButton("Button")
    button.clicked.connect(change_button_text)
    
    v_layout.addWidget(label)
    v_layout.addWidget(button)

    widget.setLayout(v_layout)

    widget.show()

    with open("theme.qss", "w") as f_obj:
        theme = f_obj.read()

    app.setStyleSheet(theme)

    sys.exit(app.exec())