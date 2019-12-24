

class Node:

    def __init__(self, value):
        self.data = value
        self.next = None
        self.randon = None

def clone(head):
    # first make copy for next pointers
    current = head
    while current is not None:
        p = Node(current.data)
        p.next = current.next
        current.next = p
        current = p.next

    # make copt for random pointers
    current = head
    while current is not None:
        current.next.random = current.random.next
        current = current.next.next
    current = head
    dup_root = head.next


    # remove the extra pointers
    while current.next is not None:
        tmp = current.next
        current.next = current.next.next
        current = tmp
    return dup_root

def print_node(head):
    while head is not None:
        print(head.data)
        head = head.next



# test case
head = Node(0)
x = Node(1)
y = Node(2)
z = Node(3)
head.next = x
head.random = z
x.next = y
x.random = head
y.next = z
y.random = z
z.random = head
z.next = None

cloned_head = clone(head)
print_node(cloned_head)
