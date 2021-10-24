from PyQt5 import QtWidgets, QtGui, QtCore
from datetime import datetime


class MainWindow(QtWidgets.QWidget):

    """ we will subclass QWidget to use it as a container """

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        container_layout = QtWidgets.QGridLayout()
        self.setLayout(container_layout) # set the layout for pur container

        self.scroll_area = QtWidgets.QScrollArea() # To get scroll widget
        
        v_scrollbar = self.scroll_area.verticalScrollBar() # get the widgets vertical scrollbar
        v_scrollbar.rangeChanged.connect(lambda: v_scrollbar.setValue(v_scrollbar.maximum()))  # automatically moves the scrollbar to the end. 
        # You will usually have to provide callable objects to connect. But since we use lambda we can use () after the method objects.

        scroll_widget = QtWidgets.QWidget() # This is the widget we will be using as inner container for scrollarea

        self.scroll_widget_layout = QtWidgets.QVBoxLayout() # we need a vertical layout to arrange the todo list vertically (instance variable so we can access this from other method, to add widgets to our layout)

        scroll_widget.setLayout(self.scroll_widget_layout) # set the scroll_layout to scroll_widget

        self.scroll_area.setWidget(scroll_widget) # sets our scroll_widget to the scroll_area.

        self.scroll_area.setWidgetResizable(True) # important.

        self.create_btn = QtWidgets.QPushButton("Create", objectName="create_btn") # the object name will help us specifically style this button, this is like giving classname/id in html, to be later styled using css
        self.create_btn.clicked.connect(self.add_todo) # when user presses button call add_todo method

        self.input_frame = QtWidgets.QFrame() # we will add inputs to the frame(a container)
        self.input_frame.setMaximumWidth(500)
        self.input_frame.setObjectName("input_frame") # This is like providing id/class name in css. This name will be used in qss to specifically style this frame
        self.frame_layout = QtWidgets.QVBoxLayout(self.input_frame)  # if you specify parent you don't need to use self.input_frame.setLayout(self.frame_layout)

        self.title_input = QtWidgets.QLineEdit()
        self.title_input.setPlaceholderText("Enter Title") # place holder text to indicate user what to enter
        self.description_input = QtWidgets.QTextEdit()
        self.description_input.setPlaceholderText("Enter description") # place holder text to indicate user what to enter

        self.datetime_input = QtWidgets.QDateTimeEdit() # Yes pyqt provides a widget to edit datetime
        self.datetime_input.setMinimumDateTime(QtCore.QDateTime.currentDateTime()) # set minimum date, Qt provides QDateTime which is just for convenience. 
        # you can get the currenttime using QDateTime.currentDateTime

        self.frame_layout.addWidget(self.title_input) # add our input widgets to the layout
        self.frame_layout.addWidget(self.description_input) 
        self.frame_layout.addWidget(self.datetime_input) 

        container_layout.addWidget(self.scroll_area, 0, 0, 2, 3)  # add the scrollarea widget to our mainlayout(container) addwidget(row-no, column-no, row-span, column-span)
        container_layout.addWidget(self.create_btn, 0, 3)
        container_layout.addWidget(self.input_frame, 1, 3)  # add the frame to the container

    def add_todo(self):

        title = self.title_input.text() # gets the text in the title input field
        description = self.description_input.toPlainText() # gets the description in the title description field
        date_time = self.datetime_input.dateTime().toString("dd/MM/yyyy hh:mm:ss") # returns string

        self.create_todo(title, description, date_time)

    def create_todo(self, title: str, description: str, date_time: str): 
        """
            we will create this method to add a new todo item in scroll area. 
            the :str after title and description are type annotation(refer internet)
        """

        widget = CustomTodoWidget(title=title)  # We will create this widget below and add to scroll layout
        widget.set_description(description=description)
        widget.set_datetime(date_time=date_time)

        self.scroll_widget_layout.addWidget(widget) # add new todo widget to the layout        


class CustomTodoWidget(QtWidgets.QWidget):
    """ This widget will have delete button and a label to display time and title """

    def __init__(self, title:str="", *args, **kwargs):
        super(CustomTodoWidget, self).__init__(*args, **kwargs) 

        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S') # we will use the current time as default for date time label

        self.date_time_lbl = QtWidgets.QLabel(current_time)
        self.title_lbl = QtWidgets.QLabel(title)

        self.description_lbl = QtWidgets.QLabel()
        self.description_lbl.hide() # initially we will hide this label and show it if show_more_button is pressed

        self.show_more_btn = QtWidgets.QPushButton("Show More")
        self.show_more_btn.setCheckable(True) # allows us to toggle between show more and show less

        self.show_more_btn.toggled.connect(self.show_more_less) # connect toggled signal to a slot. so its called when the button is toggled.

        self.delete_bnt = QtWidgets.QPushButton(clicked=self.deleteLater)
        # The clicked parameter will call deleteLater method when the button is clicked and the deleteLater method will destroy the current widget
        self.delete_bnt.setIcon(QtGui.QIcon(r"icons\delete.png")) # sets icon, pass QIcon instance

        # Now lets try to lay these widgets in our layout. We will use grid layout to make it easier for us

        grid_layout = QtWidgets.QGridLayout()
        grid_layout.addWidget(self.date_time_lbl, 0, 0) # add datetime label at row=0, column=0
        grid_layout.addWidget(self.title_lbl, 1, 0, 1, 2) # add title lable at row=1, column=0, rowspan=1, columnspan=2
        grid_layout.addWidget(self.delete_bnt, 1, 3) 
        grid_layout.addWidget(self.description_lbl, 2, 0, 1, 3) # add title lable at row=2, column=0, rowspan=1, columnspan=3

        self.setLayout(grid_layout) # set this widgets layout

    def set_description(self, description: str):
        """ sets the desctiption for descripton label """
        self.description_lbl.setText(description)

    def set_title(self, title: str):
        """ sets the title for the widget """        
        self.title_lbl.setText(title)  # sets the text on the label

    def set_datetime(self, date_time: str):
        """ set datetime """
        self.date_time_lbl.setText(date_time)

    def show_more_less(self, checked: bool):
        """
         This method will be called when the show_more_less button is clicked.
         When calling this method PyQt passes an boolean argument which tells if the button is checked or not.(You can also choose to remove the checked parameter and no error will be raised)
        """

        if checked: # if the button is checked show more.
            self.description_lbl.show()
            self.show_more_btn.setText("Show Less")  # change the button text 
        
        else:
            self.description_lbl.hide()
            self.show_more_btn.setText("Show More") # change the button text

    def title(self):
        """ return title label text """
        return self.title_lbl.text() # access text using text method
    
    def description(self):
        """ returns descriptioin text """
        return self.description_lbl.text()  
    
    def date_time(self):
        """ returns datetime """
        return self.date_time_lbl.text()
