def solution(A):
    N = len(A)
    if N == 1:
        if A[0] == 1:
            return 1
        else:
            return 0
    set_ = set()
    for i in range(N):
        if A[i] in set_:
            return 0
        set_.add(A[i])
    for i in range(1,N+1):
        if i not in set_:
            return 0
    return 1

# Test 1
print(solution([4,1,3,2]))

# Test 2
print(solution([4,1,3]))