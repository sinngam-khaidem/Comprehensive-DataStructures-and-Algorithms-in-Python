# Average time complexity of some operations involved in linked lists are:
# Look-up: O(n)
# Insert: O(n)
# Delete: O(n)
# Append: O(1)
# Prepend: O(1)

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def insert_at_index(self, data, index):
        new_node = Node(data)
        if index > self.length-1:
            self.append(data)
        elif index <= 0:
            self.prepend(data)
        else:
            curr_node = self.head
            for i in range(0, index-1):
                curr_node = curr_node.next
            new_node.next = curr_node.next
            curr_node.next = new_node
        self.length += 1

    # Reversing a linked list
    # Iterative method
    def reverse_list(self):
        if self.head == None:
            return;
        else:
            self.tail = self.head
            p = None
            q = None
            while self.head != None:
                p = self.head
                self.head = self.head.next
                p.next = q
                q = p
            self.head = p

    def print_list(self):
        if self.head == None:
            print('Empty')
        else:
            curr_node = self.head
            while curr_node != None:
                print(curr_node.data, end = " ")
                curr_node = curr_node.next
        print()

if __name__ == '__main__':
    my_ll = LinkedList()
    my_ll.append(5)
    my_ll.append(10)
    my_ll.append(-999)
    my_ll.prepend(-5656)
    my_ll.insert_at_index(20, 100)
    my_ll.print_list()
    my_ll.reverse_list()
    my_ll.print_list()
    print(my_ll.length)
    print(my_ll.head.data)
    print(my_ll.tail.data)