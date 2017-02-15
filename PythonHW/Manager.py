from Employee.py import Employee

class Manager(Employee):
    """
    One object of Manager is a subclass of the Employee class with additional instance variables "title" (a string)
    and "annual_bonus" (a float).
    """
    def __init__(self, first_name, last_name, ssn, salary, title, annual_bonus):
        """
        :param first_name: must be a string (from Employee class)
        :param last_name: must be a string (from Employee class)
        :param ssn: must be an int (from Employee class)
        :param salary: must be a flat (from Employee class)
        :param title: must be a string
        :param annual_bonus: must be a float
        initializes Manager object with correct data type
        """
        super().__init__(first_name, last_name, ssn, salary)
        if type(title) != str:
            raise TypeError("Title {0} is an invalid string.".format(title))
        elif type(annual_bonus) != float:
            raise TypeError("Annual bonus {0} is an invalid float.".format(annual_bonus))
        else:
            self.title = title
            self.annual_bonus = annual_bonus

    def __str__(self):
        """
        Returns the string form of a Manager object with data from the Employee class as well as the additional data
        "title" and "annual_bonus".
        """
        return super().__str__() + "\n Title: %s\n Annual bonus: $%.2f" %(self.title, self.annual_bonus)
