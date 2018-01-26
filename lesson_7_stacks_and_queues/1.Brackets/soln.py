def solution(S):
    N = len(S)
    if N %2 != 0:
        return 0
    stack = []
    valid = { '{' : '}', '(' : ')', '[' : ']' }
    for i in range(N):
        if S[i] in valid:
            stack.append(S[i])
        else:
            if len(stack) == 0:
                return 0
            else:
                if valid.get(stack.pop()) != S[i]:
                    return 0
    if len(stack) == 0:
        return 1
    else:
        return 0

# Test 1
print(solution('{[()()]}'))

# Test 2
print(solution('([)()]'))