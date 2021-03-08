def plusOne(A):
    A.insert(0, 0)
    i = len(A) - 1
    A[i] = (A[i] + 1) % 10
    carry = 0
    if not A[i]:
        carry = 1
    i -= 1
    while carry == 1 and i >= 0:
        A[i] = (A[i] + 1) % 10
        if A[i]:
            carry = 0
        
        i -= 1
    
    print(A if A[0] else A[1: ])

plusOne([1, 2, 3])
    
