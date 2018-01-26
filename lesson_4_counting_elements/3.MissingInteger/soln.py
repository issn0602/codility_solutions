def solution(A):
    N = len(A)
    set_ = set()
    for i in range(N):
        if A[i] > 0 and A[i] not in set_:
            set_.add(A[i])
    if len(set_) == 0:
        return 1
    for i in range(1,N+1):
        if i not in set_:
            return i
    return N+1

# Test 1
print(solution([1, 3, 6, 4, 1, 2]))

# Test 2
print(solution([1, 2, 3]))

# Test 3
print(solution([-1, -3]))