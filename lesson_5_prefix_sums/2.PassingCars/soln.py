def solution(A):
    N = len(A)
    if N < 2:
        return 0
    count = 0
    east = 0
    for i in range(N):
        if A[i] == 0:
            east +=1
        if A[i] == 1:
            count += east
    if count > 1000000000:
        return -1
    return count

# Test 1
A = [ 0, 1, 0, 1, 1 ]
print(solution(A))