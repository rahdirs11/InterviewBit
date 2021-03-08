'''
You are given an array of N integers, A1, A2 ,…, AN. Return maximum value of f(i, j) for all 1 ≤ i, j ≤ N.
f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.

For example,

A=[1, 3, -1]

f(1, 1) = f(2, 2) = f(3, 3) = 0
f(1, 2) = f(2, 1) = |1 - 3| + |1 - 2| = 3
f(1, 3) = f(3, 1) = |1 - (-1)| + |1 - 3| = 4
f(2, 3) = f(3, 2) = |3 - (-1)| + |2 - 3| = 5

So, we return 5.
'''

def maxAbsDiff(A):
    import sys
    maxDiff = -sys.maxsize - 1
    currDiff = 0
    for i in range(len(A) - 1, -1, -1):
        for j in range(i):
            currDiff = abs(A[i] - A[j]) + abs(i - j)
            maxDiff = currDiff if maxDiff < currDiff else maxDiff
        
    return maxDiff

print(maxAbsDiff([1, 3, -1]))