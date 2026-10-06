def solution(arr):
    
    answer = []
    for i in arr:  # arr에 들어있는 숫자를 처음부터 끝까지 하나씩 꺼내서 i에 저장
        if len(answer) == 0 or answer[-1] != i: # 두 조건 중 하나라도 참이면 숫자를 저장.
            # len(answer) == 0 에서 len()은 리스트의 길이를 구하는 함수.
            # 즉, answer가 비어있는지 확인. 
            # answer[-1] != i 에서 answer[-1]는 결과 리스트의 마지막 숫자를 의미. != 는 두 값이 서로 다르다는 뜻 -> 따라서 현재 숫자 i 이 마지막으로 저장한 숫자와 다르면 새로운 숫자로 판단해서 저장함.
            answer.append(i)
    return answer
