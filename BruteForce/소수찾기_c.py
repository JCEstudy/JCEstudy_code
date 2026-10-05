from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    iter = []
    nums = set()
    count = 0
    for i in numbers:
        iter.append(i)
    
    for i in range(len(iter)):
        for p in permutations(iter, i+1):
            num = int(''.join(p))
            nums.add(num)
    
    for num in nums:
        if is_prime(num):
            count += 1
                    
    return count