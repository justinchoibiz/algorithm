def solution(sticker):
    length = len(sticker);
    if length == 1:
        return sticker[0];
    
    # 1을 선택할 경우
    dp1 = [0] * length;
    dp1[0] = sticker[0];
    dp1[1] = max(sticker[0], sticker[1]);
    
    for i in range(2, length - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + sticker[i]);
    
    # 2을 선택할 경우
    dp2 = [0] * length;
    dp2[1] = sticker[1];
    
    for i in range(2, length):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + sticker[i]);
        
    return max(dp1[length - 2], dp2[length - 1]);
