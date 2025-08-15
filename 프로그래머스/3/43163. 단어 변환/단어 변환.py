from collections import deque

def compare(a, b):
    cnt = 0
    for idx, string in enumerate(a):
        if b[idx] == string:
            cnt += 1
            
    return True if cnt == len(b)-1 else False

def bfs(begin, target, words):
    queue = deque()
    queue.append([begin, 0])
    visited = {key:False for key in words}
    
    
    while queue:
        word, count = queue.popleft()
        if word == target: 
            return count;
            
        # visited[word] = True
        
        
        for other in words:
            if not visited[other] and compare(word, other):
                queue.append([other, count + 1])
                visited[other] = True
                
                
    return 0 
    

def solution(begin, target, words):
    answer = bfs(begin, target, words)
    return answer