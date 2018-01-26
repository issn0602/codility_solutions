def solution(A):
    N = len(A)
    if N < 3:
        return 0
    A.sort()
    for i in range(2,N):
        if A[i-2] + A[i-1] > A[i]:
            return 1
    return 0
    
# Test1
print(solution([ 10, 50, 1, 5 ]))