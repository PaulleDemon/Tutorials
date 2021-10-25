import sys
from PyQt5 import QtWidgets, QtCore


class CustomTimer(QtCore.QThread):

    countDownUpdated = QtCore.pyqtSignal(int) # whenever the countdown changes this signal get emitted

    def __init__(self, count_down, sleep=1000, *args, **kwargs):
        super(CustomTimer, self).__init__(*args, **kwargs)
        self.count_down = count_down
        self.sleep_time = sleep # sleep in microsecond
    

    def run(self):
        
        """ 
            This is a overridden method. 
            This method will be called when start is called. 
        """

        while self.count_down != 0:
            self.msleep(self.sleep_time)  # similar to time.sleep provided by PyQt
            self.count_down -= 1
            self.countDownUpdated.emit(self.count_down) # emits the current countdown time
            print("running...")



def update_label(count_down_time):
    """ we will update the label to show the countdown timer """
    label.setText(str(count_down_time))


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)

    label = QtWidgets.QLabel("Label")
    label.show()

    custom_count_down_timer = CustomTimer(30, 500)
    custom_count_down_timer.start() # This method will call the run method internally
    custom_count_down_timer.countDownUpdated.connect(update_label)

    sys.exit(app.exec())