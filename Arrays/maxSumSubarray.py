def maxSubarray(A):
    import sys
    currSum, maxSum = 0, -sys.maxsize - 1
    for i in A:
        currSum += i
        if currSum > maxSum:
            maxSum = currSum
        
        if currSum < 0:
            currSum = 0