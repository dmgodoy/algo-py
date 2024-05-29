def mergesort(arr: list[int]) -> list[int]:
    N = len(arr)
    if N == 0 or N == 1: return arr
    m = N // 2
    arr1 = mergesort(arr[0:m])
    arr2 = mergesort(arr[m:N])
    return merge(arr1,arr2)
def merge(arr1: list[int], arr2: list[int]) -> list[int]:
    ans = []
    i, j = 0, 0
    n, m = len(arr1), len(arr2)
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
            i += 1
        else:
            ans.append(arr2[j])
            j += 1
    ans.extend(arr1[i:n])
    ans.extend(arr2[j:m])
    return ans
arr = [3,4,1,2,7,8,3,5,7,9]
print(arr)
print(mergesort(arr))

