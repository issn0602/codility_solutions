def solution(H):
    N = len(H)
    stack = []
    count = 0
    for i in H:
        while len(stack) != 0:
            if stack[-1] > i:
                stack.pop()
            elif stack[-1] != i:
                stack.append(i)
                count += 1
            else:
                break
        else:
            stack.append(i)
            count += 1
    return count

# Test 1
print(solution([ 8, 8, 5, 7, 9, 8, 7, 4, 8 ]))