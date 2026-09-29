def solution(arr):
    answer = []
    
    for i in arr :
        # 비어있으면 넣고, 마지막 값과 다를 떄만 넣기
        if not answer or answer[-1] != i:
            answer.append(i)
    
    return answer
