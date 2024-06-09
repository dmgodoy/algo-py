class TrieNode():
    def __init__(self):
        self.children = {} # char -> TrieNode
        self.isComplete = False
        pass
    def insert(self, w: str) -> None:
        curr = self
        for c in w:
            if c in curr.children:
                curr = curr.children[c]
            else:
                curr.children[c] = TrieNode()
                curr = curr.children[c]
        curr.isComplete = True
    def search(self, w: str) -> bool:
        curr = self.startsWith(w)
        if curr:
            return curr.isComplete
    def startsWith(self, w: str) -> "TrieNode":
        curr = self
        for c in w:
            if c in curr.children:
                curr = curr.children[c]
            else: return None
        return curr
    def allStartingWith(self, w: str) -> list[str]:
        ans = []
        node = self.startsWith(w)
        def dfs(node: TrieNode, l: list[str]):
            if node.isComplete:
                ans.append(w + "".join(l))
            for k,v in node.children.items():
                l.append(k)
                dfs(v, l)
                l.pop()
        dfs(node, [])
        return ans
    
root = TrieNode()
root.insert("perro")
root.insert("pero")
root.insert("perogrullo")
root.insert("pepito")
print(root.startsWith("pe"))        # returns not None
print(root.startsWith("asdf"))      # returns None
print(root.search("pero"))          # returns True
print(root.search("per"))           # returns False
print(root.allStartingWith("per"))  # ['perro', 'pero', 'perogrullo']
