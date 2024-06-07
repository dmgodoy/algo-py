#reverse linked list
class Node():
    def __init__(self, val: int, next: "Node" = None):
        self.val = val
        self.next = next
    def __str__(self) -> str:
        arr = []
        curr = self
        while curr:
            arr.append(curr.val)
            curr = curr.next
        return ' '.join(map(str,arr))
def reverse(head: Node) -> Node:
    dummy = Node(-1, head)
    while head.next:
        next = head.next
        head.next = head.next.next
        next.next = dummy.next
        dummy.next = next
        
    return dummy.next
head = Node(1, Node(2, Node(3, Node(4))))
print(f'list:           {head}')
print(f'reversed list:  {reverse(head)}')