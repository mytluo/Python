from functools import total_ordering

@total_ordering
class Employee():
    """
    One object of Employee represents an employee with their first name, last name, social security number, and salary.
    TypeError is raised if the names aren't strings, social security number is not an int, or salary is not a float.
    """
    def __init__(self, first_name, last_name, ssn, salary):
        """
        :param first_name: must be a string
        :param last_name: must be a string
        :param ssn: must be an int
        :param salary: must be a float
        initializes Employee object with correct data type
        """
        if (type(first_name) != str) or (type(last_name) != str):
            raise TypeError("Employee name '{0}, {1}' is invalid string.".format(last_name, first_name))
        if type(ssn) != int:
            raise TypeError("Social Security Number {0} is invalid integer.".format(ssn))
        if type(salary) != float:
            raise TypeError("Salary {0} is invalid float.".format(salary))
        else:
            self.first_name = first_name
            self.last_name = last_name
            self.ssn = ssn
            self.salary = salary

    def __str__(self):
        """
        Returns a formatted string that gives the employee's name, social security number, and salary.
        """
        return "Employee: %s, %s \n SSN: %i \n Salary: $%.2f" % (self.last_name, self.first_name, self.ssn, self.salary)

    def __eq__(self, other):
        """
        Returns True if first name and last name of both objects self and other are the same, returns false otherwise
        """
        return self.first_name == other.first_name and self.last_name == other.last_name

    def __lt__(self, other):
        """
        Returns True if last name of self is alphabetically less than last name of other, return False otherwise.
        If last names of self and other are equal, returns True if first name of self is alphabetically less than
        first name of other, return False otherwise.
        """
        if self.last_name.lower() == other.last_name.lower():
            return self.first_name.lower() < other.first_name.lower()
        return self.last_name.lower() < other.last_name.lower()

    def giveRaise(self, percentRaise):
        """
        Modifies the salary of the employee with the percent (in decimal form) raise given. TypeError is raised if the
        percent raise is not a float.
        """
        if type(percentRaise) != float:
            raise TypeError("Percent raise {0} is not a valid float.".format(percentRaise))
        elif percentRaise < 0:
            raise ValueError("Percent raise cannot be negative.")
        else:
            self.salary = self.salary + (self.salary * percentRaise)
