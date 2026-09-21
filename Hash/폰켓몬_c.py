def solution(nums):
    answer = 0
    flavor = len(nums)/2
    if len(set(nums)) >= flavor:
        answer = flavor
    else:
        answer = len(set(nums))
    return answer