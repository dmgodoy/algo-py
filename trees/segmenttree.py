# calculate the sum of the range
# update values in the array

class SegmentTree():
    def __init__(self, sum: int, L: int, R: int):
        self.L = L
        self.R = R
        self.sum = sum
        self.left = None
        self.right = None
        pass
    @staticmethod
    def build(arr: list[int], L: int, R: int) -> "SegmentTree":
        if L == R:
            return SegmentTree(arr[L], L, R)
        M = (L + R) // 2
        root = SegmentTree(0, L, R)
        root.left = SegmentTree.build(arr, L, M)
        root.right = SegmentTree.build(arr, M + 1, R)
        root.sum = root.left.sum + root.right.sum
        return root

    # runtime O(log(n))
    def update(self, index: int, val: int) -> None:
        if self.L == self.R:
            self.sum = val
            return
        M = ( self.L + self.R ) // 2
        if M >= index:
            self.left.update(index, val)
        else:
            self.right.update(index, val)
        self.sum = self.left.sum + self.right.sum
    # runtime O(log(n))
    def queryRange(self, L: int, R: int) -> int:
        if self.L == L and self.R == R: return self.sum
        M = (self.L + self.R) // 2
        if M >= R:
            return self.left.queryRange(L, R)
        elif M < L:
            return self.right.queryRange(L, R)
        else:
            return (self.left.queryRange(L, M) + 
                    self.right.queryRange(M + 1, R))



t = SegmentTree.build([1,2,3,4,5],0,4)
print(f'root sum: {t.sum}')
print(f'left [{t.left.L}, {t.left.R}] sum: {t.left.sum}')
print(f'right [{t.right.L}, {t.right.R}] sum: {t.right.sum}')
print(f'query (0,3): {t.queryRange(0,3)}') # 10
print(f'query (1,3): {t.queryRange(1,3)}') #  9
print(f'query (2,3): {t.queryRange(2,3)}') #  7
print(f'query (3,4): {t.queryRange(3,4)}') #  9
t.update(3,1)
print(f'query (3,4): {t.queryRange(3,4)}') #  6