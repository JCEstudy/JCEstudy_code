# 전화번호들이 담긴 리스트 phone_book을 전달받음
# 전화번호는 문자열로 다룸. 숫자로 바꾸면 "010"처럼 앞에 붙은 0이 사라질 수 있고, 문자열이어야 앞부분을 쉽게 잘라낼 수 있음
def solution(phone_book):
    numbers = set(phone_book) #전번을 집합set으로 만들어 저장
    # 집합을 쓰는 핵심 이유는 특정 전화번호가 들어 있는지 빠르게 확인하기 위해 set은 내부적으로 해시를 사용함
		

		# 리스트에서 전번를 하나씩 꺼내 phone에 넣기
    for phone in phone_book:
		    
		    #확인할 접두어 길이 정하기
		    # range(1, len(phone))는 1부터 전번 길이보다 1 작은 수까지 반복
        # 대신 전체길이는 제외. 전체를 확인하면 자기자신이 있어서 다른 번호가 접두어인 것으로 잘못 판단하게 됨
        for length in range(1, len(phone)):
            prefix = phone[:length]
            # 전화번호의 앞부분 자르기
            #phone[:length]는 처음부터 length개 문자를 가져오는 슬라이싱임.


						# 앞부분과 일치하는 번호가 있는지 확인
            if prefix in numbers: # in은 해당 값이 들어 있는지 확인하는 연산자
                return False

# 끝까지 문제가 없으면 true 반환
# 이 코드는 두 반복문 바깥에 있어야함. 첫 번째 전번만 혹인하고 끝내지 않고, 모든 번호를 확인한 뒤 반환해야 하기 때문에
    return True
