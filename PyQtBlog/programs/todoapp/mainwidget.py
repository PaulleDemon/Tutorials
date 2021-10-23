from PyQt5 import QtWidgets, QtGui
from datetime import datetime


class MainWindow(QtWidgets.QWidget):

    """ we will subclass QWidget to use it as a container """

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(self, *args, **kwargs)

        container_layout = QtWidgets.QVBoxLayout()
        self.setLayout(container_layout) # set the layout for pur container

        self.scroll_area = QtWidgets.QScrollArea() # To get scroll widget
        
        scroll_widget = QtWidgets.QWidget() # This is the widget we will be using as inner container for scrollarea

        self.scroll_widget_layout = QtWidgets.QVBoxLayout() # we need a vertical layout to arrange the todo list vertically (instance variable so we can access this from other method, to add widgets to our layout)

        scroll_widget.setLayout(self.scroll_widget_layout) # set the scroll_layout to scroll_widget

        self.scroll_area.addWidget(scroll_widget) # adds our scroll_widget to the scroll_area.

        self.scroll_area.setWidgetResizable(True) # important to show the scroll bars
    

    def add_todo(self, title: str, description: str, date_time: str): 
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
        
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S') # we will use the current time as default for date time label

        self.date_time_lbl = QtWidgets.QLabel(current_time)
        self.title_lbl = QtWidgets.QLabel(title)

        self.description_lbl = QtWidgets.QLabel()
        self.description_lbl.hide() # initially we will hide this label and show it if show_more_button is pressed

        self.show_more_btn = QtWidgets.QPushButton("Show More")
        self.show_more_btn.setCheckable(True) # allows us to toggle between show more and show less

        self.show_more_btn.toggled.connect(self.show_more_less) # connect toggled signal to a slot. so its called when the button is toggled.

        self.delete_bnt = QtWidgets.QPushButton(icon=QtGui.QIcon(r"icons/delete.png"), clicked=self.deleteLater) # to set the icon pass an QIcon instance which takes icon-path as parameter. 
        # The clicked parameter will call deleteLater method when the button is clicked and the deleteLater method will destroy the current widget

        # Now lets try to lay these widgets in our layout. We will use grid layout to make it easier for us

        grid_layout = QtWidgets.QGridLayout()
        grid_layout.addWidget(self.date_time_lbl, 0, 0) # add datetime label at row=0, column=0
        grid_layout.addWidget(self.title_lbl, 1, 0, 1, 2) # add title lable at row=1, column=0, rowspan=1, columnspan=2
        grid_layout.addWidget(self.delete_bnt, 1, 3) 
        grid_layout.addWidget(self.description_lbl, 2, 0, 1, 3) # add title lable at row=2, column=0, rowspan=1, columnspan=3

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