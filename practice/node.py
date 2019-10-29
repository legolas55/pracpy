# Data Structures


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append_front(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node


# Helper methods for testing

def generate_linked_list_append_front(size):
    new_list = LinkedList()
    for i in range(size):
        new_list.append_front(i)
    return new_list


def print_linked_list(LinkedList):
    start = LinkedList.head
    if (start is None):
        print("Empty List")
        return
    else:
        print("Start of List")
        print(start.data)
        while (start.next_node is not None):
            start = start.get_next()
            print(start.data)
        print("End of List")


# Delete Use case for testing
def delete_middle_node_from_linked_list(LinkedList):
    #sizeoflist= 0
    middle = LinkedList.head

    if (middle is None):
        print(
            "Size of list is {0}. No Middle node to delete".format(sizeoflist))
    # elif(middle.next_node==None):
    #    sizeoflist=sizeoflist+1
    #    print("Size of Linked List is ", sizeoflist)
    #    print("Deleting Middle Node which is ", middle.data)
    else:
        one_step = LinkedList.head
        two_step = LinkedList.head
        print("add 1")
        # sizeoflist=sizeoflist+1
        while(two_step.next_node is not None and two_step.next_node.next_node is not None):
            one_step = one_step.get_next()
            # sizeoflist=sizeoflist+1
            print("add 1.5")
            # print(one_step.data)
            two_step = two_step.get_next().get_next()
            # sizeoflist=sizeoflist+1
            print("add 2")

        middle = one_step

        #print("Size of Linked List is ", sizeoflist)
        print("Deleting Middle Node which is ", middle.data)


generated_list = generate_linked_list_append_front(5)
# print(generated_list)

print_linked_list(generated_list)

print("")
delete_middle_node_from_linked_list(generated_list)

# generated_list=generate_linked_list_append_front(0)
# print_linked_list(generated_list)

# delete_middle_node_from_linked_list(generated_list)
