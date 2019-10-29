""" TO DO
"""


# Data Structures

class Node():
    """ Node Class
        The Node class contains an init, get_data, get_next and set_next methods.
        This class was designed to be used as the nodes in a singlely linked list.
    """

    def __init__(self, data=None, next_node=None):
        """ Inits node class."""
        self.data = data
        self.next_node = next_node

    def get_data(self):
        """Gets data parameter from self."""
        return self.data

    def get_next(self):
        """Gets next node of self."""
        return self.next_node

    def set_next(self, new_next):
        """Set link to next node."""
        self.next_node = new_next


class LinkedList():
    """ LinkedList Class
        The LinkedList Class is a singly linked list and has an init, append_front
        and delete mthods. In this LinkedList implimentation, nodes are appended
        at the front of the list when they are added.
    """

    def __init__(self, head=None):
        """Inits LinkedList class. """
        self.head = head

    def append_front(self, data):
        """Appends new node to the linked list as the front of the list."""
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def delete_node(self):
        """Deletes a node """


# Helper methods for testing

def generate_linked_list_append_front(size):
    """ This function generates a LinkedList object.
        Args: Size - This specifys the size of the list to create
        Return: Returns a linked list
    """
    new_list = LinkedList()
    for i in range(size):
        new_list.append_front(i)
    return new_list


def print_linked_list(linked_list):
    """This function prints a LinkedList object.
        Args: LinkedList- LinkedList object to be passed in.
        Returns: Nothing
    """
    start = linked_list.head
    if start is None:
        print("Empty List")
    else:
        print("Start of List")
        print(start.data)
        while start.next_node is not None:
            start = start.get_next()
            print(start.data)
        print("End of List")


# Delete Use case for testing
def delete_middle_node_from_linked_list(linked_list):
    """This function deletes the middle node from a singley LinkedList.
        Args: linked_list- LinkedList object to be passed in.
        Returns: Nothing
    """
    sizeoflist = 0
    middle = linked_list.head

    if middle is None:
        print(
            "Size of list is {0}. No Middle node to delete".format(sizeoflist))

    # elif(middle.next_node==None):
    #    sizeoflist=sizeoflist+1
    #    print("Size of Linked List is ", sizeoflist)
    #    print("Deleting Middle Node which is ", middle.data)

    else:
        one_step = linked_list.head
        two_step = linked_list.head
        print("add 1")
        # sizeoflist=sizeoflist+1
        while two_step.next_node is not None and two_step.next_node.next_node is not None:
            one_step = one_step.get_next()
            sizeoflist = sizeoflist + 1
            print("add 1.5")
            # print(one_step.data)
            two_step = two_step.get_next().get_next()
            sizeoflist = sizeoflist + 1
            print("add 2")

        middle = one_step

        #print("Size of Linked List is ", sizeoflist)
        print("Deleting Middle Node which is ", middle.data)


GENERATED_LIST = generate_linked_list_append_front(5)
# print(generated_list)

print_linked_list(GENERATED_LIST)

print("")
delete_middle_node_from_linked_list(GENERATED_LIST)

# generated_list=generate_linked_list_append_front(0)
# print_linked_list(generated_list)

# delete_middle_node_from_linked_list(generated_list)
