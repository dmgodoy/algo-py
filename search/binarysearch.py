def binarysearch(arr: list[int], val: int) -> int:
    l, r = 0, len(arr) - 1
    while l < r:
        m = (l + r) // 2
        if arr[m] < val:
            l = m + 1
        else: r = m
    return l if arr[l] == val else -1
print(binarysearch([0,1,2,3,4,5,6,7,8,9],6))     #6
print(binarysearch([0,1,2,3,4,5,6,7,8,9],10))    #-1
print(binarysearch([0,1,2,3,4,5,7,8,9],6))       #-1
