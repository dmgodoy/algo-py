import json
from collections import deque

def levels(n: "Node") -> list["Node"]:
    q = deque([n])
    ans = []
    while q:
        s = len(q)
        curr = []
        for i in range(s):
            n = q.popleft()
            curr.append(n.val if n else n)
            if n:
                q.append(n.left)
                q.append(n.right)
        ans.append(curr)
    return ans

def inorder(n: "Node") -> list["Node"]:
    ans = []
    def inorderHelper(n):
        if not n: return
        if n.left: inorderHelper(n.left)
        ans.append(n.val)
        if n.right: inorderHelper(n.right)
    inorderHelper(n)
    return ans

def inorderI(n: "Node") -> list["Node"]:
    stack, ans = [], []
    curr = n
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        ans.append(curr.val)
        curr = curr.right
    return ans

def preorder(n: "Node") -> list["Node"]:
    ans = []
    def preorderHelper(n):
        if not n: return
        ans.append(n.val)
        if n.left: preorderHelper(n.left)
        if n.right: preorderHelper(n.right)
    preorderHelper(n)
    return ans


def preorderI(n: "Node") -> list["Node"]:
    ans, stack = [], [n] 
    while stack:
        curr = stack.pop()
        if not curr: continue
        ans.append(curr.val)
        stack.append(curr.right)
        stack.append(curr.left)

    return ans

def postorder(n: "Node") -> list["Node"]:
    ans = []
    def postorderHelper(n):
        if not n: return
        if n.left: postorderHelper(n.left)
        if n.right: postorderHelper(n.right)
        ans.append(n.val)
    postorderHelper(n)
    return ans

def postorderI(n: "Node") -> list["Node"]:
    stack, visit, ans = [n], [True], []
    while stack:
        curr, v = stack.pop(), visit.pop()
        if not curr: continue
        if v:
            visit.append(False)
            stack.append(curr)
            visit.append(True)
            stack.append(curr.right)
            visit.append(True)
            stack.append(curr.left)
        else: ans.append(curr.val)
    return ans

def postorderI2(n: "Node") -> list["Node"]:
    prev, stack, ans = None, [n], []
    first = True
    while stack:
        curr = stack.pop()
        if not curr: continue
        if first or (prev != curr and prev != curr.right):
            stack.append(curr)
            stack.append(curr.right)
            stack.append(curr.left)
        elif prev == curr or prev == curr.right:
            ans.append(curr.val)
        first = False
        prev = curr
    return ans

class Node():
    def __init__(self, val: int, left: "Node" = None, right: "Node" = None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return str(levels(self))
n = Node(-1)
left = Node(1)
right = Node(2)
n.left = left
n.right = right
right.left = Node(3)
right.right = Node(4)
print(f'levels: {n}')
print(f'inorder: {inorder(n)}')
print(f'inorder (iter.): {inorderI(n)}')
print(f'preorder: {preorder(n)}')
print(f'preorder (iter.): {preorderI(n)}')
print(f'postorder: {postorder(n)}')
print(f'postorder (iter.): {postorderI(n)}')
print(f'postorder (iter. 2): {postorderI2(n)}')

