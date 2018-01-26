def solution(A):
    N = len(A)
    val = -1
    count = 0
    pos = -1
    for i in range(N):
        if count == 0:
            val = A[i]
            pos = i
            count += 1
        else:
            if A[i] == val:
                count += 1
            else:
                count -= 1
    count = 0
    for i in range(N):
        if A[i] == val:
            count += 1
    if count > (N//2):
        return pos
    else:
        return -1

# test 1
print(solution([ 3, 4, 3, 2, 3, -1, 3, 3]))