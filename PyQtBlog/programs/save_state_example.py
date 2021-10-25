import sys
import os
from PyQt5 import QtWidgets, QtGui


class SampleWidget(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super(SampleWidget, self).__init__(*args, **kwargs)
        
        self.setLayout(QtWidgets.QVBoxLayout()) # adds widget to the layout 

        self.check_box = QtWidgets.QCheckBox("Dark Theme?")
        self.button = QtWidgets.QPushButton("The Button is not clicked", clicked=self.change_btn_text) # on button click the change_btn_text method will be called

        self.layout().addWidget(self.check_box) # the self.layout() returns the instance of the widgets layout on which you can use addWidget()
        self.layout().addWidget(self.button)

    def change_btn_text(self):
        """ We will use this method to change the button text """

        button_text = self.button.text() # This method return the button text

        if button_text == "The Button is not clicked":
            self.button.setText("The Button is clicked")

        else:
            self.button.setText("The Button is not clicked")


    def save(self):
        """ we will implement saving in this method """
        checked = self.check_box.isChecked() # isChecked method returns True or false.
        btn_text = self.button.text()

        checked = int(checked) # we will save "0" for False and "1" for True, you cannot save integer so convert it to string(I'll be using f-string as shown below).

        with open("save_state.txt", "w") as f_obj: # f_obj is simply file object
            f_obj.write(f"{checked}\n")
            f_obj.write(btn_text)

    def load(self):
        """ load the file and set the state in this method """
        
        checked = False # default
        button_text = "The Button is not clicked" #default

        if os.path.exists("save_state.txt"): #Checks if the file exists, it will be better to use try-except block here.s
            with open("save_state.txt", "r") as f_obj:
                checked, button_text = f_obj.readlines() # This will return a list which will then be unpacked

        self.check_box.setChecked(bool(int(checked))) # first convert it to int then to boolean as setChecked expect a boolean (You can also just pass int(checked)) 
        self.button.setText(button_text)

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        """ This method will be called before the widget is destored, you can 
        override this method to do cleanup or saving before deatroying the widget. 
        """
        self.save()
        super(SampleWidget, self).closeEvent(event) # close it after saving the state to the file


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)

    widget = SampleWidget()
    widget.load()
    widget.show()

    sys.exit(app.exec())