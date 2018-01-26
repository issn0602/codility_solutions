def solution(A):
    N = len(A)
    A.sort()
    return max( A[N-3]*A[N-2]*A[N-1], A[N-1]*A[1]*A[0])

# Test 1
print(solution([ - 3, 1, 2, -2, 5, 6 ]))