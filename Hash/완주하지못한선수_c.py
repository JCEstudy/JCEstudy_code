def solution(participant, completion):
    answer = ''
    count = {}
    for name in participant:
        count[name] = count.get(name, 0) + 1
    
    for del_name in completion:
        count[del_name] = count.get(del_name, 0) - 1
    
    for key, value in count.items():
        if value == 1:
            answer = key

    return answer