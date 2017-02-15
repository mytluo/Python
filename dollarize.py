# not using PEP 0378
import string, traceback
def dollarize(floatnum):
	""" takes in a float and returns it in the dollar format """
    # rounds float to 2 decimal places and converts to string format
    str_num = str("%.2f") % floatnum
    sign = ""
    # if there is a sign assign it to variable and separate from the digits
    if str_num[0] not in string.digits:
        sign = str_num[0]
        str_num = str_num[1:]
    # separate the decimal and numbers to its right from the numbers to its left    
    decimals = str_num[-3:]
    # convert separated number on right hand side to list and reverse it to add commas as needed
    list_float = list(reversed(str_num[:-3]))
    if len(list_float) > 3:
        # start index at 3 where the first comma would go
        i = 3
        end = len(list_float)
        while i < end:
            list_float.insert(i, ",")
            # next index of comma, if it exists
            i += 4
            # because list was altered, need to increment length of list to accurately track positions of commas needed
            end += 1
    # reverse list with commas added and join back together        
    str_num = ''.join(reversed(list_float))
    # return full number with sign (if exists) and decimal precision points
    if sign:
        return "%s$%s%s" %(sign, str_num, decimals)
    else:
        return "$%s%s" %(str_num, decimals)
