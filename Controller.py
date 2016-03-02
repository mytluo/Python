from tkinter import *

class MyFrame(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.entry_label = Label(self, text="Temperature")
        self.entry_label.pack(side=LEFT, fill=BOTH, expand=1)
        self.temp_entry = Entry()
        self.temp_entry.pack(side=LEFT, fill=BOTH, expand=1)

        self.Tf_to_Tc = Button(self, text="Convert Fahrenheit to Celcius", command=self.getTc)
        self.Tf_to_Tc.pack(fill=BOTH, expand=1)

        self.Tc_to_Tf = Button(self, text="Convert Celcius to Fahrenheit", command=self.getTf)
        self.Tc_to_Tf.pack(fill=BOTH, expand=1)

        self.quitButton = Button(self, text="Quit", command=self.quit)
        self.quitButton.pack(side=BOTTOM, fill=BOTH, expand=1)

    def getTc(self):
        try:
            Tf = float(self.temp_entry.get())
            Tc = (5/9.)*(Tf-32)
            self.answer_label = Label(self, text="{0}°F is equivalent to {1:.1f}°C".format(Tf, Tc))
            self.answer_label.pack(fill=BOTH, expand=1)
        except:
            self.bad_entry = Label(self, text="Please enter a number only.")
            self.bad_entry.pack(fill=BOTH, expand=1)

    def getTf(self):
        try:
            Tc = float(self.temp_entry.get())
            Tf = ((9/5.)*Tc)+32
            self.answer_label = Label(self, text="{0}°C is equivalent to {1:.1f}°F".format(Tc, Tf))
            self.answer_label.grid()
        except:
            self.bad_entry = Label(self, text="Please enter a number only.")
            self.bad_entry.grid()

if __name__ == '__main__':
    root = Tk()
    root.title("Convert Temperature")
    app = MyFrame()
    app.mainloop()
    root.destroy()
