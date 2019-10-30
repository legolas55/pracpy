""" Write a method that answers the following problem:
Accept as input:
·       list: a singly-linked list
Remove the middle element of the list without iterating the list more than once.
Assume the list size cannot be known until traversed.
Support your answer with tests.
"""

### Assumptions
# 1.
# 2.


### Data Structures
# Would improve on data structure choice on the next iteration.
# Array lists seem to be faster than linked list with Nodes.
# Every time a node is created, 

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

    def delete_node(self, data):
        """Deletes a node by looking at self.data value"""
        current_node=self.head
        previous_node=None
        found_node = False
        while current_node and found_node is False:
            if current_node.get_data() == data:
                found_node = True
            else:
                previous_node = current_node
                current_node = current_node.get_next()
            if current_node is None:
                raise ValueError("Data not in list")
            if previous_node is None:
                self.head=current_node.get_next()
            else:
                previous_node.set_next(current_node.get_next())
        
        

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
# FUT- Function Under Test
def delete_middle_node_from_linked_list(linked_list):
    """This function deletes the middle node from a singley LinkedList.
        Args: linked_list - LinkedList object to be passed in.
        Returns: Nothing
    """
    sizeoflist = 0
    middle = linked_list.head

    if middle is None:
        print("Size of list is {0}. No Middle node to delete"
              .format(sizeoflist))
    else:
        one_step = linked_list.head
        two_step = linked_list.head

        #Since there is a head node, size must be at least 1
        sizeoflist=sizeoflist+1
        #print("add 1")
    
        #The condition is structured like this to avoid a NoneType error for two_step
        #This could be written as while(true) and except a NoneType error, but not recommended
        #Look before you leap is better in this situation
        while two_step.next_node is not None and two_step.next_node.next_node is not None:
            one_step = one_step.get_next()
            sizeoflist = sizeoflist + 1
            #print("add 1.5")
            #print(one_step.data)
            two_step = two_step.get_next().get_next()
            sizeoflist = sizeoflist + 1
            #print("add 2")

        #Two_step pointing at a node with a next node but no next next node
        #Since calculating size of list, need edge case for correct size.
        if two_step.next_node is not None:
            sizeoflist=sizeoflist+1

        #This is the middle node
        middle = one_step
        
        print("Size of Linked List is ", sizeoflist)
        print("Deleting Middle Node which is ", middle.data,"\n")

        linked_list.delete_node(middle.data)

        print("\n")
        print_linked_list(linked_list)
        print("\n")
        
        return linked_list


#This could be made into a decorator
def test_delete_middle_node(size_list):
    """ This function will generate a singly linked list of size size_list,
        print the list and test the delete_middle_node_from_linked_list function.
    """ 
    GENERATED_LIST = generate_linked_list_append_front(size_list)
    print_linked_list(GENERATED_LIST)
    delete_middle_node_from_linked_list(GENERATED_LIST)
    

#Unit Tests

# Case Null List 
test_delete_middle_node(0)

#Case Only Head Node
test_delete_middle_node(1)

#Case Two Nodes not triggering the loop, Test size edge case.
test_delete_middle_node(2)

#Case Test Loop
test_delete_middle_node(3)

#Keep going
test_delete_middle_node(6)





