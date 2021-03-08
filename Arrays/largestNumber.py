class Solution:
    def compare(self, right, left):
        return int(str(right) + str(left)) > int(str(left) + str(right))

    def largestNumber(self, A):
        A = sorted(A, reverse=True, key=lambda right, left: int(str(right) + str(left)) > int(str(left) + str(right)))
        print(A)


print(Solution().largestNumber([int(x) for x in input().split()]))