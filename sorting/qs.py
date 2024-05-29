def partition(arr: list[int], l: int, r:int) -> None:
    pivot = arr[l]
    lo, hi = l + 1, r
    while lo < hi:
        while lo <= hi and arr[lo] < pivot: lo += 1 #strict comparison is important for cases with repeated elements
        while lo <= hi and arr[hi] > pivot: hi -= 1 #idem
        if lo < hi:
            arr[lo], arr[hi] = arr[hi], arr[lo]
    if arr[l] > arr[hi]:
        arr[l], arr[hi] = arr[hi], arr[l]
        return lo 
    return hi 
def qs(arr: list[int], l: int, r:int) -> None:
    if l >= r: return
    p = partition(arr, l, r)
    qs(arr,l,p-1)
    qs(arr,p+1,r)

arr = [3,4,1,2,7,8,3,5,7,9]
print(arr)
print(qs(arr, 0, len(arr)-1))
print(arr)

