def Solution(N):
    val = bin(N)[2:]
    print(val)
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

print(Solution(1041))