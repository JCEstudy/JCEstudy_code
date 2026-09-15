def solution(array, commands):
    answer = []
    
    for command in commands:
        start, end, k = command
        
        temp = array[start - 1:end]
        temp.sort()
        
        answer.append(temp[k-1])
        
    return answer
