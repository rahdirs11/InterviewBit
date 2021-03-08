A = [int(x) for x in input().split()]
special = int()

while True:
    oddSum, evenSum = 0, 0
    for i, num in enumerate(A):
        if not i % 2:
            evenSum += num
        else:
            oddSum += num
    
    print(oddSum, evenSum)
    for i, num in enumerate(A):
        if i % 2 and oddSum > evenSum:
            if oddSum - num == evenSum:
                print('odd, \t', num)
                A.remove(num)
                special += 1
                break
        elif evenSum > oddSum and not i % 2:
            print('even:\t', num)
            if evenSum - num == oddSum:
                A.remove(num)
                special += 1
                break
        print(oddSum, evenSum, end='\n==================\n')
    else:
        print('Ran completely')
        break

print(special)
