"""This
"""

# 2D list generation

LIST_A = ["hello", 1.5, 5, "world"]
LIST_B = ["this", "place", "is", 6.7]
LIST_C = [12, "grand", 8, -1]
LIST_D = ["great", "scott", 11, "world"]

LIST_ALL = [LIST_A, LIST_B, LIST_C, LIST_D]


# function to find a interger in a list and display list


def find_integer_in_list_of_list(list_to_search, integer):
    """ This function will find an integer in a list of lists and return a list.
        Args: list_to_search - the list of list to search
              integer - the integer to find in the list of list
        Returns: List that integer was found in.
    """

    if isinstance(integer, int) is False:
        print(
            " {0} is not an integer. Please choose an integer to look for".format(integer))
    elif isinstance(list_to_search, list) is False:
        print(" That does not appear to be a list. Please choose a list to search")

    for lists in list_to_search:
        for element in lists:
            if element == integer:
                print("found")
                print(lists)
                return True

    print("Integer was not in the list")
    return False


# Unit Tests

find_integer_in_list_of_list(LIST_ALL, 2.2)
find_integer_in_list_of_list(5, 2)
find_integer_in_list_of_list(LIST_ALL, 10)
find_integer_in_list_of_list(LIST_ALL, 11)
