import sys, traceback
def total_after_tax(amount, tax=9.25):
    """ takes in an amount and optional tax rate (default 9.25%) and returns total after tax """
    initial = float(amount)
    tax = 1 + (float(tax)/100)
    return "Your total is $%.2f" % (initial * tax)
if __name__ == '__main__':
    amount = input("Enter amount before tax: $")
    tax = input("Enter sales tax, or hit 'enter' for default rate of 9.25%: %")
    try:
        if not tax:
            print(total_after_tax(amount))
        else:
            print(total_after_tax(amount, tax))
    except ValueError:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print("print_tb:")
        traceback.print_tb(exc_traceback)
        print("print_exception:")
        traceback.print_exception(exc_type, exc_value, exc_traceback)
