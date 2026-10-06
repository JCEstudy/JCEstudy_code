# 핵심
# 참가자 명단에서 완주한 사람을 빼고, 남은 한 사람의 이름을 찾는 문제.
# 동명이인이 있을 수 있으므로, 이름마다 몇 명인지 세는 게 중요

# 두 개의 리스트를 전달받는 함수
# paricipant: 마라톤에 참가한 사람들의 이름
# completion : 마라톤을 완주한 사람들의 이름
def solution(paricipant, completion):
			counts = {} # 이름별 인원수를 저장할 딕셔너리
			# 딕셔너리에는 이름이 키(key), 인원수가 값(value)
		
		
		# 참가자를 한 명씩 확인
		for name in paricipant:  # participant에서 이름을 하나씩 꺼내 name에 넣어
				counts[name] = counts.get(name,0) + 1 # 해당 이름의 인원수 1 증가시키기
				# counts.get(name,0)이 핵심
				# name이 딕셔너리에 있으면 -> 저장된 인원수를 가져옴
				# name이 없으면 -> 기본값 0을 가져옴
				# 가져온 숫자에 1을 더해서 다시 저장
			
			
		# 완주한 사람을 한 명씩 확인
		for name in completion: # 완주자 리스트에서 이름을 하나씩 꺼냄
				counts[name] -= 1 # 완주한 사람의 인원수 1 감소시키기
				# (counts[name] = counts[name] - 1과 같은 의미
				#--> 완주한 사람이 확인되면 해당 이름을 남은 인원수를 한 명 줄임
		
		
		 # 남은 사람이 있는 이름 찾기
		for name in counts: # 딕셔너리를 이렇게 반복하면 키인 이름을 하나씩 꺼냄. 인원수를 꺼내는 게 아니라는 점 기억하기
				if counts[name] > 0: # 인원수가0보다 크면 아직 완주자로 처리되지 않은 사람이 있다는 뜻
						return name # 그 이름을 return으로 반환하고 함수를 끝냄
				
