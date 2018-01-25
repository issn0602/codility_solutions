def solution(A,K):
    if len(A) < 2:
        return A
    N = len(A)
    if K > N:
        K = K%N
    return A[-K:] + A[:-K]

# Test 1
print(solution([3, 8, 9, 7, 6],3))

# Test 2
print(solution([0, 0, 0], 1))

# Test 3
print(solution([1, 2, 3, 4], 4))