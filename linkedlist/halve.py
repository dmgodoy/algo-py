class Node():
    def __init__(self, val: int, next: "Node" = None):
        self.val = val
        self.next = next
    def __str__(self):
        arr = []
        curr = self
        while curr:
            arr.append(curr.val)
            curr = curr.next
        return ' '.join(map(str, arr))
def halve(head: Node) -> tuple[Node, Node]:
    dummy = Node(-1, head)
    slow, fast = dummy, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    prev = slow
    slow = slow.next
    prev.next = None
    #slow.next, slow = None, slow.next
    return (head, slow)

head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(f'list: {head}')
head1, head2 = halve(head)
print(f'head1: {head1}')
print(f'head2: {head2}')

