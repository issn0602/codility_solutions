# A = 1 , C = 2, G = 3, T = 4

def solution(S, P, Q):
    
    N = len(S)
    M = len(P)
    
    marr = [0] * M
    
    for i in range(M):
        sstr = S[P[i]:Q[i]+1]
        print(sstr)
        if 'A' in sstr:
            marr[i] = 1
        elif 'C' in sstr:
            marr[i] = 2
        elif 'G' in sstr:
            marr[i] = 3
        elif 'T' in sstr:
            marr[i] = 4