import sys
from PyQt5 import QtWidgets, QtGui, QtCore


class CustomLabel(QtWidgets.QLabel):

    def __init__(self, *args, **kwargs):
        super(CustomLabel, self).__init__(*args, **kwargs)
        self.start_point = QtCore.QPoint(0, 0) # This is x, y point, we will use Qpoint to represent it
        self.end_point = QtCore.QPoint(0, 0) # The QPoint will only take two integers, QPointF for floating point

        self._draw_rect = False
    
    def mousePressEvent(self, event: QtGui.QMouseEvent): 
        """
        This method will be called with event parameter which will have all the inormation about the event, such as mouse position, mouse button(left, right or middle) etc.
        This method will be called whenever there is a mouse press event
        """
        super(CustomLabel, self).mousePressEvent(event)

        self._draw_rect = True # We have an if condition in the paintEvent. If this is True the paint method will draw the rectangle

        self.start_point = event.pos()  # event.pos() returns QPoint which is the position of the mouse press

    def mouseMoveEvent(self, event: QtGui.QMouseEvent):
        """
            This method will be called whenever the mouse moves
        """
        super(CustomLabel, self).mouseMoveEvent(event)
        self.end_point = event.pos() # This will return the current mouse position
    
    def mouseReleaseEvent(self, event: QtGui.QMouseEvent):
        """
            This method will be called whenever the mouse is released.
            This method is not necessary for this program(only to demonstrate)
        """
        super(CustomLabel, self).mouseReleaseEvent(event)
        self.end_point = event.pos() # This will get the mouse position when the button was released


    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        """
            This method will be called whenever a key is pressed.
        """
        super(CustomLabel, self).keyPressEvent(event)

        if event.key() == QtCore.Qt.Key_Escape: # The Qt class contains constants such as Key_Escape for esc key, you have many more key constants in it such as Key_A, for A key etc.
            self._draw_rect = False # In the next loop in the paint event the rectangle will not be drawn


    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        """ 
            This method is use to paint the widget. This method is responsible for the text and drawings, 
            on our widget.
            This method will always be called once in an event loop(That is very often)
        """
        super(CustomLabel, self).paintEvent(event) # if you call super after painter the label will be drawn over our paint, so keep it in the beginning

        if self._draw_rect:
            painter = QtGui.QPainter(self) # you will have to create a painter instance and pass the widget on which you want to draw, in our case its the same widget, hence we pass self.

            painter.setBrush(QtGui.QColor("red")) # This will set your paint brush with which we will fill our border
            painter.setPen(QtGui.QColor()) # This will be our border color(outline)

            painter.drawRect(QtCore.QRect(self.start_point, self.end_point)) # The QRect will store 4 points of a rectangle(or two QPoints). You could also have stored it in a list, but the draw_rect method expects a QRect instance.

        self.update() # we will have to update the paint so the rectangle is visible


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    widget = CustomLabel("Sample Text")
    widget.show()

    sys.exit(app.exec())