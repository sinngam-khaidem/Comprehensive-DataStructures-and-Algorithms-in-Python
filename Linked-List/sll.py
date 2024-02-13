from typing import List, Optional

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

# Add a node a the beginning of the linked list
def add_at_beg(head: Node, data: int) -> Node:
    new_node = Node(data)
    new_node.next = head
    head = new_node
    return head

# Add a node at the end of the linked list
def add_at_end(head: Node, data: int) -> Node:
    new_node = Node(data)
    if head == None:
        head = new_node
    else:
        temp = head
        while temp.next != None:
            temp = temp.next
        temp.next = new_node
    return head

# Add a node at the specified index
def add_at_index(head: Node, data: int, index: int) -> Node:
    if index <= 0:
        return add_at_beg(head, data)
    temp = head
    for i in range(0, index-1):
        if temp != None:
            temp = temp.next
    if temp == None:
        return add_at_end(head, data)
    else:
        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node
        return head


# Display all the nodes of a linked list
def display_nodes(head: Node) -> Node:
    temp = head
    while temp != None:
        print(temp.data, end = " ")
        temp = temp.next
    print()

# Reversing a linked list
# Iterative method
def reverse_list(head):
    if head != None:
        p = None
        q = None
        while head != None:
            p = head
            head = head.next
            p.next = q
            q = p
        head = p
    return head


# Delete duplicates from a sorted linked list
def deleteDuplicates(head: Node) -> Node:
    if head != None and head.next != None:
        curr_val = head.val
        front = head.next
        back = head
        while front != None:
            if front.val == curr_val:
                back.next = front.next
                front.next = None
                front = back.next
            else:
                curr_val = front.val
                back = front
                front = front.next
    return head

# Merge two sorted linked list
def mergeTwoLists(self, list1: Node, list2: Node) -> Node:
    dummy = curr_node = ListNode()
    while list1 != None and list2 != None:
        if list1.val >= list2.val:
            curr_node.next = list2
            list2 = list2.next
        else:
            curr_node.next = list1
            list1 = list1.next
        curr_node = curr_node.next
    if list1 == None:
        curr_node.next = list2
    else:
        curr_node.next = list1
    return dummy.next

# Check Loop
def hasCycle(self, head: Optional[ListNode]) -> bool:
    if head == None:
        return False
    fast = slow = head
    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Add Two Numbers
def addTwoNumbers(self, l1: Node, l2: Node) -> Node:
    dummy = curr_node = ListNode(0)
    while l1 != None or l2 != None:
        x = l1.val if l1 is not None else 0
        y = l2.val if l2 is not None else 0
        sum = x + y + dummy.val
        carry = sum // 10
        target = sum % 10
        dummy.val = carry
        curr_node.next = ListNode(target)
        curr_node = curr_node.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    if dummy.val != 0:
        curr_node.next = ListNode(dummy.val)
    return dummy.next

if __name__ == "__main__":
    head = Node(10)
    head = add_at_end(head, 20)
    head = add_at_end(head, 30)
    head = reverse_list(head)
    display_nodes(head)