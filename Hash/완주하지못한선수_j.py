# 해시로 풀이
from collections import Counter

def solution(participant, completion):
    # 참가자와 완주자의 이름별 등장 횟수를 각각 센 후,
    # 참가자 수에서 완주자 수를 빼면 완주하지 못한 선수만 남음
    answer = Counter(participant) - Counter(completion)

    # 남은 선수의 이름(Key)을 리스트로 변환한 뒤 첫 번째 값 반환
    return list(answer.keys())[0]


# 정렬로 풀이
def solution(participant, completion):
    
    p = sorted(participant) # 이름 순 정렬
    c = sorted(completion)  # 이름 순 정렬
    
    
    for i in range(len(c)): # 완주자 배열 길이만큼 반복문 돌아
        if p[i] != c[i]:    # 참가자[i]와 완주자[i]가 다르다면 
            
            return p[i]     # 참가자[i]가 완주 못한 선수

    return p[-1]            # 모든 경우가 동일하다면 마지막 참가자가 완주 못한 선수
