def solution(progresses, speeds):
    days = [] # 각 기능이 며칠 뒤에 완성되는지 저장하려고 빈 리스트 만듦

    # 각 작업이 완료되기까지 필요한 날짜 계산
    for i in range(len(progresses)): # len(progresses)는 리스트의 길이를 구함. ex) len([93, 30, 55]) 얘는 길이가 3임 o, 1, 2
        # 즉, i가 차례대로 0 -> 1 -> 2 가 되면서 모든 작업을 확인
        
        day = 0   # day는 완료까지 며칠 걸렸는지 세는 변수
        progress = progresses[i]  #현재 작업의 진행률을 가져옴
        # i = 0 이면 progress = progress[0] 이므로 progress = 93 인것

        # 100%가 될때까지 작업 진행 (while 문은 조건이 참인 동안 계속 반복)
        while progress < 100:
            progress += speeds[i] #progress = progress + speeds[i]
            day += 1 #day = day + 1

        days.append(day)

     # 뒤에 있는 기능이 먼저 완성되어도 앞 기능이 완성되지 않았다면 먼저 배포할 수 없음.
    answer = []
    count = 1
    first = days[0]

    # 배포할 기능끼리 묶기
    for i in range(1, len(days)):
        if days[i] <= first:
            count += 1
        else:
            answer.append(count)
            count = 1
            first = days[i]

    answer.append(count)

    return answer
