def solution(A):
    N = len(A)
    if N == 0:
        return 0
    if N == 1:
        return 1
    if N == 2:
        if A[0] == A[1]:
            return 1
        else:
            return 2
    set_ = set()
    for i in range(N):
        if A[i] not in set_:
            set_.add(A[i])
    return len(set_)

# Test 1
print(solution([2,1,1,2,3,1]))