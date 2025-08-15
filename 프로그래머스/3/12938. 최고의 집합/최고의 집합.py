def solution(n, s):
    m = s // n;
    n_ = s % n;
    answer = [m] * n;
    
    if m == 0:
        answer = [-1];
    elif n_ != 0:
        for idx in range(n_):
            answer[idx] += 1;
        
    answer.sort();
    return answer;
        