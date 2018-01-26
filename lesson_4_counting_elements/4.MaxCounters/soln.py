def solution(N, A):
    alen = len(A)
    count = [0]*N
    mval = 0
    cmax = 0
    for i in range(alen):
        if 1 <= A[i] <= N:
            if count[A[i]-1] <= mval:
                count[A[i]-1] = mval + 1
            else:
                count[A[i]-1] += 1
            if count[A[i]-1] > cmax:
                cmax = count[A[i]-1]
        if A[i] == N+1:
            mval = cmax
    for i in range(N):
        if count[i] < mval:
            count[i] = mval
    return count

# Test 1
A = [ 3, 4, 4, 6, 1, 4, 4 ]
N = 5
print(solution(N,A))