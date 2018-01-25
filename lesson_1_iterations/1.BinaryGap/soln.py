def solution(N):
    val = bin(N)[2:]
    current = 0
    count = 0
    for i in val:
        if i == '1':
            if count > current:
                current = count
            count = 0
        if i == '0':
            count += 1
    return(current)

# Test 1
print(solution(1041))

#Test 2
print(solution(15))