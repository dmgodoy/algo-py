# given an array, return true if there are two elements within a window of size k that are equal

def closeDuplicatesBruteForce(arr: list[int], k: int) -> bool:
    for l in range(0, len(arr) - k + 1):
        for r in range(l + 1, min(l + k, len(arr))):
            if arr[l] == arr[r]:
                return True
    return False

def closeDuplicates(arr: list[int], k: int) -> bool:
    window = set()
    l = 0
    for r in range(0, len(arr)):
        if r - l + 1 > k:
            window.remove(arr[l])
            l += 1
        if arr[r] in window:
            return True
        window.add(arr[r])
    return False

print(closeDuplicates([1,2,3,4,5,6,7,8],2)) # False
print(closeDuplicates([1,2,3,4,5,6,7,8],3)) # False
print(closeDuplicates([1,2,3,4,5,4,7,8],2)) # False
print(closeDuplicates([1,2,3,4,5,4,7,8],3)) # True


