import string
def strip_whitespace(str_to_strip):
    """ returns string stripped of leading and trailing whitespace """
    to_list = list(str_to_strip)
    start = 0
    end = 0
    for i, chr in enumerate(to_list):
        if chr not in string.whitespace:
            start = i
            break
    for i, chr in enumerate(reversed(to_list)):
        if chr not in string.whitespace:
            end = i
            break
    return ''.join(to_list[start:(len(to_list)-end)])
if __name__ == '__main__':
    print("\tHello world! \n ")
    print(strip_whitespace("\tHello world! \n "))
    print("newline stripped")
