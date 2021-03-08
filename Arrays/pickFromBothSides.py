'''Given an integer array A of size N.

You can pick B elements from either left or right end of the array A to get maximum sum.

Find and return this maximum possible sum.

NOTE: Suppose B = 4 and array A contains 10 elements then:

You can pick first four elements or can pick last four elements or can pick 1 from front and 3 from back etc . you need to return the maximum possible sum of elements you can pick.
'''

def solve(A, B):
    currSum = int()
    for i in range(B):
        currSum += A[i]
    
    res = currSum
    if len(A) == B:
        return res

    for i in range(1, B + 1):
        print(f'A[len(A) - i] = {A[len(A) - i]} || A[B - i] = {A[B - i]}')
        currSum = currSum - A[B - i] + A[len(A) - i]
        print(f"currSum = {currSum}")
        res = max(currSum, res)
    return res


print(solve([5, -2, 3, 1, 2], 3))