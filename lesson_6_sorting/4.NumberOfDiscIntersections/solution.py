def solution(A):
    N = len(A)
    mxarr = [0]*N
    mnarr = [0]*N
    for i in range(N):
        mnarr[i] = i - A[i]
        mxarr[i] = i + A[i]
    mxarr.sort()
    mnarr.sort()
    li = 0
    count = 0
    for ui in range(0,N):
        while li < N and mxarr[ui] >= mnarr[li]:
            li += 1
        count += li - ui - 1
    if count > 10000000:
        return -1
    return count
    
# Test 1
print(solution([ 1, 5, 2, 1, 4, 0 ]))