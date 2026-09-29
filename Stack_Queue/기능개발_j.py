def solution(progresses, speeds):
    answer = []
    
    day = 0
    count = 0
    
    while progresses: 
        # 맨 앞 작업이 100% 가 됐을 때
        if(progresses[0] + day * speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        
        # 맨 앞 작업이 100% 미만일 때
        else :
            if count > 0:
                answer.append(count)
                count = 0
            day += 1
            
    answer.append(count)
            
    return answer
