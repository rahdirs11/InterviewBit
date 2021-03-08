import sys

def solve(A: list):
    minVal, maxVal = sys.maxsize, -sys.maxsize - 1
    for a in A:
        if a < minVal:
            minVal = a
        if a > maxVal:
            maxVal = a
    
    return minVal + maxVal


print(solve(list(map(int, input().split()))))