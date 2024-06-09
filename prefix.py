# query the sum of a subarray of values
class Query():

    def __init__(self, arr: list[int]):
        if len(arr) == 0: raise Exception("Empty array!")
        self.arr = arr
        self.prefix = [arr[0]]
        for i in range(1, len(arr)):
            self.prefix.append(self.prefix[-1] + arr[i])

    def query(self, l: int, r: int) -> int:
        sum = 0
        for i in range(l, r + 1):
            sum += self.arr[i]
        return sum
    def queryOptimized(self, l: int, r: int) -> int:
        sum = self.prefix[r]
        if l > 0:
            sum -= self.prefix[l - 1]
        return sum

q = Query([1,2,3,4,5,6])
print(q.query(1,2)) # 5
print(q.query(1,4)) # 14
print(q.queryOptimized(1,2)) # 5
print(q.queryOptimized(1,4)) # 14
Query([]) # exception

