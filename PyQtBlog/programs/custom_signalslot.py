import sys
from PyQt5 import QtWidgets, QtCore, QtGui



class ClickableLabel(QtWidgets.QLabel):

    # you will have to specify how many arguments and the type of the argument(eg: bool, int, str), in
    # our case we will use QPoint to pass mouse position. 
    # All your signals must be class level, not object level/instance level. 
    clicked = QtCore.pyqtSignal(QtCore.QPoint)  

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        super(ClickableLabel, self).mousePressEvent(event)

        self.clicked.emit(event.pos()) # we will emit the signal and pass the position


def print_label_click_pos(pos):
    print(pos)


if __name__ == '__main__':
    
    app = QtWidgets.QApplication(sys.argv)

    label = ClickableLabel("Sample label")
    label.clicked.connect(print_label_click_pos)  # connect the signal to a slot
    label.show()
    
    sys.exit(app.exec())