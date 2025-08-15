import heapq

def solution(n, works):
    
    q = []
    for time in works:
        heapq.heappush(q, -time);
    
    for _ in range(n):
        if not q:
            break;
        longest_time = - heapq.heappop(q);
        longest_time -= 1;
        if longest_time > 0:
            heapq.heappush(q, -longest_time);
    result = 0;
    while q:
        result +=  heapq.heappop(q) ** 2;
        
    return result;