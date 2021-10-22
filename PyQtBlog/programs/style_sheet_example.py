import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout


def change_button_text():
    button.setText("Button has been clicked")


if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    widget = QWidget()
    widget.setStyleSheet("background-color: #f5fbff;")

    v_layout = QVBoxLayout()

    label = QLabel("Sample label")
    label.setStyleSheet("""
                        color: black;
                        background-color: transparent;
                        font-size: 25px;
                        font-family: Times;
                            """)

    button = QPushButton("Button")
    button.clicked.connect(change_button_text)
    button.setStyleSheet("""
                        color: white;
                        background-color: blue;
                        font-size: 20px;
                        font-family: Times;
                        border-radius: 10px;
                        padding: 5px;
                            """)
    
    v_layout.addWidget(label)
    v_layout.addWidget(button)

    widget.setLayout(v_layout)

    widget.show()

    sys.exit(app.exec())