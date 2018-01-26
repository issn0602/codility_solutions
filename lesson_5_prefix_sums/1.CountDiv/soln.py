def solution(A, B, K):
    if A%K == 0:
        return ( B//K - A//K + 1 )
    else:
        return ( B//K - A//K )

# Test 1
A, B, K = 6, 11, 2
print(solution(A,B,K))