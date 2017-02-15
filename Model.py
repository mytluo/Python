class ConvertTemp:
    """ ConvertTemp class is the Model in the MVC architecture. It defines the functions to convert a temperature
        from Fahrenheit to Celcius or Celcius to Fahrenheit and returns the converted temperature.
    """
    def getTc(self, temp):
        """ Takes in a temperature as an int or float and calculates the corresponding temperature in Celcius.
        """
        try:
            self.Tf = float(temp)
            self.Tc = (5/9.)*(self.Tf-32)
            return self.Tc
        except:
            pass

    def getTf(self, temp):
        """ Takes in a temperature as an int or float and calculates the corresponding temperature in Fahrenheit.
        """
        try:
            self.Tc = float(temp)
            self.Tf = ((9/5.)*self.Tc)+32
            return self.Tf
        except:
            pass
