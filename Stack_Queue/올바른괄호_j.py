def solution(s):
    answer = []
    
    for i in s: 
        if i == '(':
            answer.append(i) 
            
        else:
            if not answer: # 스택이 비어있다면 false
                return False
            answer.pop() # 쌍이 있다면 pop
            

    return len(answer) == 0
