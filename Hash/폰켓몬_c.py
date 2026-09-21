from collections import Counter

def solution(nums):
    answer = min(len(nums)/2, len(Counter(nums).items()))
    return answer