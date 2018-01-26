def solution(A,B):
    N = len(A)
    if N == 1:
        return 1
    stack = []
    count = 0
    for i in range(N):
        if B[i] == 0:
            while len(stack) != 0:
                if stack[-1] > A[i]:
                    break
                else:
                    stack.pop()
            else:
                count += 1
        else:
            stack.append(A[i])
    return count+len(stack)

print(solution([4,3,2,1,5],[0,1,0,0,0]))