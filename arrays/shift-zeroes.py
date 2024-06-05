# shift all 0s to the end of the array
def shiftZeroes(arr: list[int]) -> None:
    pos = 0
    for n in arr:
        if n != 0:
            arr[pos] = n
            pos += 1
    for i in range(pos, len(arr)):
        arr[i] = 0

arr = [1,2,3,0,5,6,0,0,7,8,9]
print(f'before: {arr}')
shiftZeroes(arr)
print(f'after: {arr}')
