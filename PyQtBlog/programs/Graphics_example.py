import sys
from PyQt5 import QtGui, QtWidgets


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)

    view = QtWidgets.QGraphicsView()
    scene = QtWidgets.QGraphicsScene()  
    view.setScene(scene)  # add scene to the view (Think of it like attaching the canvas to the board)
    
    line = QtWidgets.QGraphicsLineItem(20, 30, 100, 200) # provide x1, y1, x2, y2

    scene.addItem(line) #add line to the scene

    scene.addLine(100, 50, 250, 200, QtGui.QColor("red"))
    scene.addRect(50, 50, 100, 100) 

    view.show() 

    sys.exit(app.exec())