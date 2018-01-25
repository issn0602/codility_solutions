def solution(A):
    N = len(A)
    if N == 2:
        return abs(A[0]-A[1])
    lsum = A[0]
    rsum = sum(A[1:])
    diff = abs(lsum-rsum)
    print(diff)
    i=1
    while i < (N-1):
        lsum += A[i]
        rsum -= A[i]
        temp = abs(lsum-rsum)
        print(diff)
        if temp < diff:
            diff = temp
        i+=1
    return(diff)

# Test
print(solution([3,1,2,4,3]))