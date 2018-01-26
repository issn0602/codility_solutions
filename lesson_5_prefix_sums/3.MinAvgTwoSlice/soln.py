from sys import maxsize

def solution(A):
    N = len(A)
    if N == 2:
        return 0
    vmin = maxsize
    loc = 0
    for i in range(N-1):
        temp = ( A[i] + A[i+1] ) / 2
        if temp < vmin:
            vmin = temp
            loc = i
    for i in range(N-2):
        temp = ( A[i] + A[i+1] + A[i+2] ) / 3
        if temp < vmin:
            vmin = temp
            loc = i
    return loc

# Test 1
A = [ 4, 2, 2, 5, 1, 5, 8 ]
solution(A)