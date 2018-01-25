def solution(A):
    res = set()
    for i in A:
        if i in res:
            res.remove(i)
        else:
            res.add(i)
    res = res.pop()
    return res

# Test 1
print(solution([9, 3, 9, 3, 9, 7, 9]))