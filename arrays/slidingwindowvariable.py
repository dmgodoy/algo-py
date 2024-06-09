# find the length of the longest subarray, with the same value in each position
def longestSubarray(arr: list[int]) -> int:
    l = maxLen = 0
    for r in range(0, len(arr)):
        if arr[l] != arr[r]:
            l = r
        maxLen = max(maxLen, r - l + 1) 
    return maxLen

# find the min length sub array where the sum is >= target. All values are positive
def minSubarray(arr: list[int], target: int) -> int:
    l, currSum, minLen = 0, 0, float("inf")
    for r in range(0, len(arr)):
        currSum += arr[r]
        while currSum >= target:
            minLen = min(minLen, r - l + 1)
            currSum -= arr[l]
            l += 1
        
    return 0 if minLen == float("inf") else minLen

print(longestSubarray([1,2,3,3,3,6,3,8])) # 3
print(longestSubarray([1,2,3,4,5,6,7,8])) # 1

print(minSubarray([1,2,3,3,3,6,3,8], 3)) # 1
print(minSubarray([1], 10)) # 0


