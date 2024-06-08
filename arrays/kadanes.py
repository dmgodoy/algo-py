# find max sum subarray
# kadanes return max sum
def maxSum(arr: list[int]) -> int:
    maxSum, currSum = float("-inf"), 0
    for n in arr:
        currSum = max(currSum, 0)
        currSum += n
        maxSum = max(currSum, maxSum)
    return maxSum
# kadanes return max sum subarray
def maxSumSubarray(arr: list[int]) -> int:
    maxSum, currSum, maxL, maxR, L = float("-inf"), 0, 0, 0, 0
    for R in range(0, len(arr)):
        if currSum < 0:
            L = R
            currSum = 0
        currSum += arr[R]
        if currSum > maxSum:
            maxL, maxR = L, R
            maxSum = currSum
    return arr[maxL:maxR+1]

print(maxSum([1,2,3,-2,1,2,3])) #10
print(maxSumSubarray([1,2,3,-2,1,2,3])) # [1,2,3,-2,1,2,3]

print(maxSum([1,2,3,-7,2,2,3])) #7
print(maxSumSubarray([1,2,3,-7,2,2,3])) # [2,2,3]
