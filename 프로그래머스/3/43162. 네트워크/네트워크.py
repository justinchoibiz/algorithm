def solution(n, computers):
    answer = 0;
    visited = [False] * n;
    
    def dfs(computer_idx):
        visited[computer_idx] = True;
        for neighbor_idx in range(n):
            if computers[computer_idx][neighbor_idx] == 1 and not visited[neighbor_idx]:
                dfs(neighbor_idx)
    
    for i in range(n):
        if not visited[i]:
            dfs(i);
            answer += 1;    
    return answer;