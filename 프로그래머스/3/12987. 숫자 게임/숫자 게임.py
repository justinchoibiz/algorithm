def solution(A, B):
    A.sort(reverse=True)
    B.sort(reverse=True)
    i = 0;
    for a in A:
        if a < B[i]:
            i += 1; 
    return i;