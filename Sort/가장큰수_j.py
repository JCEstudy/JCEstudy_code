from functools import cmp_to_key

def solution(numbers):
    # 숫자를 문자열로 변환
    # → 두 숫자를 이어 붙여서 크기를 비교하기 위해 필요
    numbers = list(map(str, numbers))

    # 두 숫자의 순서를 결정하는 비교 함수
    def compare(a, b):
        # a를 앞에 놓은 경우와 b를 앞에 놓은 경우를 비교
        # 예: a="3", b="30"
        # "330" > "303" 이므로 3을 앞에 배치
        if a + b > b + a:
            return -1
        else:
            return 1

    # compare 함수를 기준으로 정렬
    numbers.sort(key=cmp_to_key(compare))

    # 정렬된 문자열을 하나로 이어 붙여서 반환
    return ''.join(numbers)
