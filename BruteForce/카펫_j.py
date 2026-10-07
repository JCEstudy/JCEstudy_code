def solution(brown, yellow):
    
    # x는 가로, y는 세로
    for y in range(1, yellow + 1):
        if yellow % y == 0: 
            x = yellow // y

        if x >= y:
            if (2 * x) + (2 * y) + 4 == brown:
                return [x+2, y+2]
