def isPalindrome(str: str) -> bool:
    l, r = 0, len(str) - 1
    while l < r:
        if str[l] != str[r]:
            return False
        l += 1
        r -= 1
    return True
def sortedTwoSum(arr: list[int], target: int) -> tuple[int]:
    l, r = 0, len(arr) - 1
    while l < r:
        if arr[l] + arr[r] == target: return (l, r)
        if arr[l] + arr[r] > target:
            r -= 1
        else: l += 1
    return (-1, -1)

print(isPalindrome("asddsa"))   #True
print(isPalindrome("asdsa"))    #True
print(isPalindrome("ab"))       #False
print(isPalindrome(""))         #True

print(sortedTwoSum([-1,2,3,4,5,7,8], 8)) # (2, 4)
