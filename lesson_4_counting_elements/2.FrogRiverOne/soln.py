def solution(X, A):
    N = len(A)
    count = 0
    set_ = set()
    for i in range(N):
        if 1 <= A[i] <= X and A[i] not in set_:
            set_.add(A[i])
            count += 1
        if count == X:
            return i
    return -1

# Test 1
print(solution(5,[1,3,1,4,2,3,5,4]))