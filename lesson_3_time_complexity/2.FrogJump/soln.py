def solution(X,Y,D):
    if (Y-X) % D == 0:
        return int ( (Y-X) / D )
    else:
        return int ( ( (Y-X) // D ) + 1 )

# Test 1
print(solution(10, 85, 30))

# Test 2
print(solution(1, 5, 2))