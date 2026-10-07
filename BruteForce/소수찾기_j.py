from itertools import permutations

# 소수 판별 함수
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
		nums = set()
		
    # 가능한 조합 만들기 
    for k in range(1, len(numbers) + 1):
        for p in permutations(numbers, k):
            nums.add(int("".join(p)))
            
    # 소수 개수 세기
    count = 0
    for num in nums:
        if is_prime(num):
            count += 1
            
    return count

