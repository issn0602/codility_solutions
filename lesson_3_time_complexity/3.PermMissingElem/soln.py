def solution(A):
    N = len(A)
    if N == 0:
        return 1
    asum = sum(A)
    accsum = int((N+1)*(N+2)/2)
    return accsum-asum

# Test 1
print(solution([2,3,1,5]))