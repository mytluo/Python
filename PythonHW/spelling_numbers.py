# Assignment: Spelling Numbers

import math

""" spell() takes in an integer, positive or negative, and returns the corresponding word.
    The function first checks that the argument passed is an int. If not, the code terminates.
    The absolute value of the int is stored in a separate variable "num_abs" to work with just the int itself without
        any signs.
    If the (original) int is less than 0, the variable "sign" is assigned "negative." Otherwise "sign" remains empty.
    The function then checks if the int is 0, as that is the only time "zero" will be spelled out; otherwise, the int
        is stored as a list of lists, where each inner list holds up to 3 values. Each inner list essentially acts as
        a comma separator.
    The inner list is then passed to the function num_to_words() in reverse in a for loop so the function operates on
        a single inner list at a time. The variable "sublist_counter" is also passed into the function to keep track
        of which inner list the for loop is passing to num_to_words() so the appropriate scale (hundred, thousand,
        million) can be assigned. This necessitates the inner lists being iterated in reverse so we can assign the
        correct scale depending on the digit's position in the overall integer.
    The return value of num_to_words(), if it is not empty, is prepended to the list "num_words" and sublist_counter
        increments by 1. When the for loop has iterated over all inner lists in "num_list_of_lists," the resulting
        strings stored in "num_words" are joined together, and concatenated with the "sign" variable to return the
        fully spelled out integer.
"""
def spell(num):
    if not isinstance(num, int) or math.isnan(num):
        return "Not an integer."
    sign = ""
    spelled_num = ""
    num_abs = int(math.fabs(num))
    if num < 0:
        sign = "negative "
    if num == 0:
        return "zero"
    else:
        num_list_of_lists = create_list_of_lists(str(num_abs))
        num_words = []
        sublist_counter = 0
        for sublist in reversed(num_list_of_lists):
            if num_to_words(sublist, sublist_counter):
                num_words.insert(0, num_to_words(sublist, sublist_counter))
            sublist_counter += 1
        spelled_num = ' '.join(num_words)
    return sign + spelled_num


""" num_to_words() takes in a list and a integer as arguments and returns a string of the spelled out numbers in the
        list, including the appropriate scale depending on each digit's position in the integer passed into spell().
    The list is a set of three or less broken down from the aforementioned integer, and is also reversed to easily
        determine the digit's position in the complete integer.
    If the entire list consists only of 0's, the function returns an empty value, as there is no unique word to return.
    If the second inner list is being passed to num_to_words(), then the integer is in the thousands and the word is
        inserted into the list "num_word_list." If it is the third inner list, "million" is inserted.
    If there is at least two digits in the list and the digit in the tens place is not 0, then the two digits are joined
        together so it can be passed into the deca() function.
    Enumerating through the list while tracking the digit and the index position it's in, the for loop determines which
        dictionary function to call on.
    If the digit is in the ones place (index == 0), it calls on the single_digits() function, unless it is part of the
        deca() function call in "deca_arg," and/or is 0.
    Index == 1 is in the tens place, which calls on the deca() dictionary using the joined together tens and ones digits
        in "deca_arg."
    Index == 3 is in the hundreds place, and calls on both single_digits() and appends the scale "hundred" to the
        "num_word_list" dictionary.
    After each digit has returned the correct word appended or inserted into "num_word_list," the function returns a
        string that joins together all the words in the list.
"""
def num_to_words(num_sublist, sublist_counter):
    if len(num_sublist) == 3 and num_sublist[0] == num_sublist[1] == num_sublist[2] == 0:
        return
    num_word_list = []
    reversed_list = num_sublist[::-1]
    deca_arg = ""
    if sublist_counter == 1:
        num_word_list.insert(2, "thousand")
    if sublist_counter == 2:
        num_word_list.append("million")
    for index, digit in enumerate(reversed_list):
        try:
            if reversed_list[index+1] and reversed_list[index+1] != 0:
                deca_arg = (''.join(str(digit) for digit in num_sublist[-2:]))
        except:
            pass
        if index == 1 and digit != 0:
            num_word_list.insert(0, deca(deca_arg))
        if index == 0 and digit != 0:
            if len(deca_arg) != 2 and digit != 0:
                num_word_list.insert(0, single_digits(digit))
            else:
                continue
        if index == 2 and digit != 0:
            num_word_list.insert(0, single_digits(digit))
            num_word_list.insert(1, "hundred")
    return ' '.join(num_word_list)


""" create_list_of_lists() takes in an int (converted to a string) and creates a list of lists grouped in a set of 3
        or less, starting from the end of the int.
    A "loop_control" variable stores how many inner lists to create by dividing the length of the int in string form
        (which would be the total number of digits), and rounding it up to the next whole number using math.ceil()
        function. This ensures that there is always one inner list generated, and int with 4 to 6 digits have 2 inner
        lists created ("loop_control" is 2) and ints with 7 to 9 digits have 3 inner lists ("loop_control" is 3).
    Because we want to skip the last set of 3 digits that have already been stored in the previous iteration,
        "index_start" sets the multiplier for the start index (with -3, to ensure a max set of 3 elements in an inner
        list), and "index_stop" sets the index so we do not include digits that have already been iterated over.
    A while loop is executed with a nested for loop to iterate over each set of 1, 2, or 3 digits and store them in a
        list, which is then appended to the main outer list "num_list_of_lists." The function returns this outer list,
        with all inner lists in order as the number itself appeared.
"""
def create_list_of_lists(num_str):
    num_list_of_lists = []
    loop_control = int(math.ceil(len(num_str)/3.0))
    index_start = 1
    index_stop = len(num_str)
    while loop_control > 0:
        num_list = []
        for i in reversed(num_str[-3*index_start:index_stop]):
            num_list.insert(0, int(i))
        num_list_of_lists.insert(0, (num_list))
        index_start += 1
        index_stop += -3
        loop_control -= 1
    return num_list_of_lists


""" single_digits() takes in a single digit integer and returns the corresponding word for one through nine.
    The ones_scale dictonary maps each int between 1 and 9 to its corresponding word. The function takes the argument
        being passed as the key to look for in the dictionary and returns the corresponding value.
"""
def single_digits(num_str):
    ones_scale = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine"
    }
    return ones_scale[int(num_str)]


def deca(num_str):
    deca_scale = {
        1: {
            0: "ten",
            1: "eleven",
            2: "twelve",
            3: "thirteen",
            4: "fourteen",
            5: "fifteen",
            6: "sixteen",
            7: "seventeen",
            8: "eighteen",
            9: "nineteen"
        },
        2: "twenty",
        3: "thirty",
        4: "forty",
        5: "fifty",
        6: "sixty",
        7: "seventy",
        8: "eighty",
        9: "ninety"
    }
    if int(num_str[0]) == 1:
        return deca_scale[int(num_str[0])][int(num_str[1])]
    else:
        if int(num_str[1]) == 0:
            return deca_scale[int(num_str[0])]
        else:
            return deca_scale[int(num_str[0])] + " " + single_digits(num_str[1])
