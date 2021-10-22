import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout


_style = """
        QWidget{
            background-color: #f5fbff;
        }

        QLabel{
            color: black;
            background-color: transparent;
            font-size: 25px;
            font-family: Times;
        }

        QPushButton{
            color: white;
            background-color: #3db1ff;
            font-size: 20px;
            font-family: Times;
            border-radius: 10px;
            padding: 5px;
        }

        QPushButton:hover{
            background-color: #2a7ab0;
        }

        """

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
    app.setStyleSheet(_style)

    sys.exit(app.exec())