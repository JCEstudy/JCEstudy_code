import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    left = deque()
    
    for i, j in zip(progresses, speeds):
        left.append(math.ceil((100-i)/j))
    

    count = 0
    temp = left[0]
    
    for i in left:
        if temp >= i:
            count += 1
        else:
            answer.append(count)
            temp = i
            count = 1
    answer.append(count)

    return answer