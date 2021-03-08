'''
-> you can move in any one of the 8 directions: up, down, right, left, diagonal(TR, TL, DR, DL)
-> sequence of points have been given
-> so you have to cover every single point
-> check for movement in the following order:
    -> diagonal
    -> cardinal directions (u, d, l, r)
-> increment the number of steps by one at each step
'''

def coverPoints(A, B):
    curr = [A[0], B[0]]
    i = 1
    moves = 0
    while i < len(A):
        moves += max(abs(A[i] - A[i - 1]), abs(B[i] - B[i - 1]))
        i += 1
    print(moves)

coverPoints([ 4, 8, -7, -5, -13, 9, -7, 8 ], [ 4, -15, -10, -3, -13, 12, 8, -8 ])

