def solution(n, computers):
    answer = 0;
    visited = [False] * n;
    
    def dfs(c_idx):
        visited[c_idx] = True;
        for n_idx in range(n):
            if computers[c_idx][n_idx] == 1 and not visited[n_idx]:
                dfs(n_idx);
    for i in (range(n)):
        if not visited[i]:
            dfs(i);
            answer += 1;
            
    return answer;