# Assignment 10: Graphical User Interface
from tkinter import *
import Model.py, View,py

class Controller:
    """ The Controller for the Convert Temperature GUI app that follows the MVC architecture.
        When the user presses a Button on the View, this Controller calls the corresponding method in
        the Model. It then adds a new Label in the app containing the temperature conversion result.
    """

    def __init__(self):
        """ Starts the Tk framework with title "Convert Temperature", instantiates the Model ConvertTemp,
            instantiates the View MyFrame, and starts the event loop that waits for the user to press a
            Button on the View (after entering text in the Entry).
        """
        root = Tk()
        root.title("Convert Temperature")
        self.model = mluozhang_Model.ConvertTemp()
        self.view = mluozhang_View.MyFrame(self)
        self.view.mainloop()
        root.destroy()

    def Tf_to_Tc(self, temp):
        """ Calls the method getTc() from the Model when the user presses the Tf_to_Tc button
            ("Convert Fahrenheit to Celcius"). Creates a new Label to display the results of
            the conversion.
        """
        self.Tc = self.model.getTc(temp)
        if isinstance(self.Tc, float):
            print_string = "{0}°F is equivalent to {1:.1f}°C".format(temp, self.Tc)
        else:
            print_string = "Please input a number."
        self.answer = Label(self.view, text=print_string)
        self.answer.grid(sticky=S)
        self.clear_text()

    def Tc_to_Tf(self, temp):
        """ Calls the method getTf() from the Model when the user presses the Tc_to_Tf button
            ("Convert Celcius to Fahrenheit"). Creates a new Label to display the results of
            the conversion.
        """
        self.Tf = self.model.getTf(temp)
        if isinstance(self.Tf, float):
            print_string = "{0}°C is equivalent to {1:.1f}°F".format(temp, self.Tf)
        else:
            print_string = "Please input a number."
        self.answer = Label(self.view, text=print_string)
        self.answer.grid(sticky=S)
        self.clear_text()

    def clear_text(self):
        """ Clears the text in the Entry field.
        """
        self.view.temp_entry.delete(0, END)

""" Main program to initiate the Controller.
"""
if __name__ == "__main__":
    c = Controller()
