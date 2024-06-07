class Node():
    def __init__(self, val: int, next: "Node" = None):
        self.val = val
        self.next = next
    def __str__(self) -> str:
        return str(self.val)

def hasCycle(n: Node) -> bool:
    slow = fast = n
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    
    if slow != fast: return None

    start = n
    while start != slow:
        start = start.next
        slow = slow.next
    return slow

def printHasCycle(head: Node):
    r1 = hasCycle(head)
    print(f'cycle? {"starting in " + str(r1.val) if r1 else False}') #None

last = Node(5)
head = Node(1, Node(2, Node(3, Node(4, last))))
printHasCycle(head) # False
last.next = head
printHasCycle(head) # Starting in 1


