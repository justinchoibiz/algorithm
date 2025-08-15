def solution(routes):
    
    answer = 0;
    car_pos = -30001;
    routes.sort(key=lambda x:x[1]);
    
    for route in routes:
        car_in = route[0];
        car_out = route[1];
        
        if car_in > car_pos:
            answer += 1;
            car_pos = car_out
    return answer;