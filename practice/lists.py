""" Write a method that answers the following problem:
Accept as input:
·       list: an unordered list of arrays each with 4 elements.
·       target: an integer
Find and display the complete array that contains the provided target number.
"""


# Python Version 3.7.5
# Written and Tested In IDLE
# Pep8 compliance using autopep8 && adapts from Google's python style guide
# Pylint score of 9.79/10
# This file is designed to be run as a whole

# Assumptions
# 1. Args might not be lists


# Data Structures
# Would improve on data structure choice on the next iteration.
# Array lists seem to be faster than linked list with Nodes.


import sys
import os

# 2D list generation
# Different Entries that could break the function

LIST_A = ["hello", 1.5, 5, "world"]
LIST_B = ["this", "place", "is", 6.7]
LIST_C = [12, "grand", 8, -1]
LIST_D = ["great", (3, 5), 11, "world"]
LIST_E = []

DICT_A = {
    "starbucks:coding",
    "walmart:shopping",
    "table:manners",
    "think:tank"}
TUPLE_A = ("hello", 2)

LIST_ALL = [LIST_A, LIST_B, LIST_C, LIST_D]

LIST_MIX = [LIST_A, LIST_B, LIST_C, DICT_A]

LIST_MIX_2 = [LIST_A, LIST_B, "hello", "you"]

LIST_MIX_3 = [LIST_A, LIST_B, TUPLE_A, "you"]

LIST_MIX_4 = [LIST_A, LIST_B, 1, "you"]

LIST_MIX_5 = [LIST_E, LIST_E, LIST_E, LIST_E, ]

# function to find a interger in a list and display list
# Function under Test


def find_integer_in_list_of_list(list_to_search, integer):
    """ This function will find an integer in a list of lists and return a list.
        Args: list_to_search - the list of list to search
              integer - the integer to find in the list of list
        Returns:True -  Prints List that integer was found in.
                False - Integer was not found
                2 - Non integer was passed in as an Arg
                3 - Non list was passed in as an Arg
                4 - Sub list contains a non list element
    """

    if isinstance(integer, int) is False:
        print("Return code 2: {0} is not an integer. Please choose an integer to look for"
              .format(integer))
        return 2
    if isinstance(list_to_search, list) is False:
        print("Return Code 3: That does not appear to be a list. Please choose a list to search")
        return 3

    for lists in list_to_search:
        if isinstance(lists, list) is False:
            print("Return Code 4: That does not appear to be a list in the main list")
            return 4

        for element in lists:
            if element == integer:
                print("Sucess, The integer was found in the following list:")
                print(lists)
                return True

    print("Integer was not found")
    return False


# Unit Tests
# Should all pass and the goal is to incur no exceptions
try:
    # Case decimal instead of integer
    find_integer_in_list_of_list(LIST_ALL, 2.2)

    # Case input non list argument
    find_integer_in_list_of_list(5, 2)

    # Case integer is not present in any lists
    find_integer_in_list_of_list(LIST_ALL, 10)

    # Case success integer is found
    find_integer_in_list_of_list(LIST_ALL, 11)

    # Case dictionary instead of list
    find_integer_in_list_of_list(LIST_MIX, 11)

    # Case string instead of list
    find_integer_in_list_of_list(LIST_MIX_2, 11)

    # Case Tuple and string instead of list
    find_integer_in_list_of_list(LIST_MIX_3, 11)

    # Case integer and string instead of list
    find_integer_in_list_of_list(LIST_MIX_4, 11)

    # Case all empty lists
    find_integer_in_list_of_list(LIST_MIX_5, 11)

    print("All Tests Passed")
except Exception as error:
    EXC_TYPE, EXC_OBJ, EXC_TB = sys.exc_info()
    F_NAME = os.path.split(EXC_TB.tb_frame.f_code.co_filename)[1]
    print(error, EXC_TYPE, F_NAME, EXC_TB.tb_lineno)
