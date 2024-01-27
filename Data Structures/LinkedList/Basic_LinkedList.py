class Node:
    def __init__(self, data=None, next_val=None):
        self.data = data
        self.next = next_val


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        self.head = Node(data, self.head)

    def append(self, data):
        if self.head is None:
            self.head = Node(data=data)
        itr = self.head
        while itr.next is not None:
            itr = itr.next
        itr.next = Node(data=data)

    def print_list(self):
        curr = self.head
        if curr is None:
            print("Linked List is empty")
        while curr is not None:
            print(f'{curr.data}', end=" --> ")
            curr = curr.next
        print("\n<-- End of LinkedList -->\n")

    def get_length(self):
        length = 0
        if self.head is None:
            print("Linked List is empty")
        itr = self.head
        while itr is not None:
            length += 1
            itr = itr.next
        print(f"Length of Linked List is {length}")
        return length

    def delete(self, value):
        if self.head is None:
            print("Linked List is empty")
        itr = self.head
        if itr.data == value:
            self.head = self.head.next
            return
        while itr.next is not None:
            if itr.next.data == value:
                itr.next = itr.next.next
                return
            itr = itr.next
        print("Value is not in Linked List")

    def insert(self, index, value):
        if index < 0 or index >= self.get_length():
            raise IndexError("Index out of range")
        if index == 0:
            self.insert_head(value)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = Node(value, itr.next)
                return
            itr = itr.next
            count += 1

    def insert_all(self, values):
        for data in values:
            self.append(data)



llist = LinkedList()
llist.print_list()
llist.insert_head(10)
llist.print_list()
llist.delete(10)
llist.print_list()
llist.get_length()
llist.insert_head(20)
llist.insert_head(30)
llist.insert_head(40)
llist.insert_head(987)
llist.append(40)
llist.append(200)
llist.insert_head(302)
llist.insert_head(143)
llist.print_list()
llist.get_length()
llist.delete(20)
llist.print_list()
llist.get_length()
llist.delete(2)
llist.print_list()
llist.insert(5, 5)
llist.print_list()
llist.insert_all([33,44,55,66,77])
llist.print_list()
