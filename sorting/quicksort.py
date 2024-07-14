def partition(arr: list[int], l: int, r:int) -> None:
    pivot = arr[r]
    pivot_index = l
    for i in range(l,r):
        if arr[i] <= pivot:
            arr[i],arr[pivot_index]=arr[pivot_index],arr[i]
            pivot_index += 1
    arr[r],arr[pivot_index]=arr[pivot_index],arr[r]
    return pivot_index
def qs(arr: list[int], l: int, r:int) -> None:
    if l >= r: return
    p = partition(arr, l, r)
    qs(arr,l,p-1)
    qs(arr,p+1,r)

arr = [4,1,3,2,7,8,9,6,6]#[3,4,1,2,7,8,3,5,7,9]
print(arr)
qs(arr, 0, len(arr)-1)
print(arr)

