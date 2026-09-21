def solution(phone_book):
    # 전화번호를 모두 set에 저장
    phone_set = set(phone_book)

    # 각 전화번호의 앞부분을 하나씩 확인
    for phone in phone_book:
        for i in range(1, len(phone)):
            prefix = phone[:i]

            # 이 prefix가 다른 전화번호로 존재하면 다른 번호의 접두사
            if prefix in phone_set:
                return False

    # 모든 전화번호를 확인했는데 접두사가 없으면
    return True
