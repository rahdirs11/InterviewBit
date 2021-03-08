class Solution:
    def solve(self, A):
        i, j = 0, len(A) - 1
        output = [0 for _ in range(len(A))]
        index = len(A) - 1
        while i < j:
            if abs(A[i]) >= abs(A[j]):
                output[index] = A[i] ** 2
                i += 1
            else:
                output[index] = A[j] ** 2
                j -= 1
            
            index -= 1
        
        output[index] = A[i] ** 2
        return output

    
for o in Solution().solve(list(map(int, input().split()))):
    print(o, end=" ")

print()