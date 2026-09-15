def solution(citations):
    
    # 인용 횟수 큰 순서대로 정렬
    citations.sort(reverse=True)
    
    h_index = 0
    
    # 논문 순서대로 확인
    for i in range(len(citations)):
        rank = i + 1
        citation_count = citations[i]

        # 인용 횟수가 논문 개수(rank) 이상이면 h_index 갱신
        if citation_count >= rank:
            h_index = rank
        else:
            break
    
    return h_index
