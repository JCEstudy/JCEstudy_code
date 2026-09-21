def solution(nums):
    
    # 중복 제거 후 폰켓몬 종류
    kinds = set(nums)
    
    # 가져갈 수 있는 폰켓몬 수
    max_count = len(nums) // 2
    
   # 종류 수와 가져갈 수 있는 수 중 작은 값 반환
    return min(len(kinds), max_count)
