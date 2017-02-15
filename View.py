from tkinter import *

class MyFrame(Frame):
    """ MyFrame class is the View in the MVC architecture. This View class is a tkinter.Frame that contains
        3 buttons, 1 Label, and 1 Entry for user input. Two of the Buttons will notify the Controller if
        they are pressed, and the last Button quits the app. The Label labels the Entry field to inform
        the user to enter a number as an input. The Entry takes in this input.
    """
    def __init__(self, controller):
        """ Initiates the Frame that spans 4 rows and 5 columns.
        """
        Frame.__init__(self)
        self.grid(rowspan=4, columnspan=5)
        self.controller = controller
        self.createWidgets()

    def createWidgets(self):
        """ Creates the 3 buttons, Label, and Entry field.
        """
        self.entry_label = Label(self, text="Temperature \n(as a number):")
        self.entry_label.grid(sticky=NE, padx=20, pady=15)
        self.temp_entry = Entry()
        self.temp_entry.grid(row=0, column=3, pady=15, sticky=NE)

        self.Tf_to_Tc = Button(self, text="Convert Fahrenheit to Celcius",
                               command=lambda: self.controller.Tf_to_Tc(self.temp_entry.get()))
        self.Tf_to_Tc.grid(row=3, column=1, columnspan=2, padx=10, pady=5, sticky=SW)

        self.Tc_to_Tf = Button(self, text="Convert Celcius to Fahrenheit",
                               command=lambda: self.controller.Tc_to_Tf(self.temp_entry.get()))
        self.Tc_to_Tf.grid(row=4, column=1, columnspan=2, padx=10, pady=5, sticky=SW)

        self.quitButton = Button(self, text="Quit", command=self.quit)
        self.quitButton.grid(column=2, sticky=SE, padx=5, pady=5)

