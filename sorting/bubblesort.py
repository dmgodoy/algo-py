def bubblesort(arr: list[int]) -> None:
    N = len(arr)
    for i in range(N):
        for j in range(i+1,N):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]

arr = [3,4,1,2,7,8,3,5,7,9]
print(arr)
bubblesort(arr)
print(arr)

