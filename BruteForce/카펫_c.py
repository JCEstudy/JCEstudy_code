def solution(brown, yellow):
    answer = []
    
    for w in range(1, yellow + 1):
        if yellow % w == 0:
            h = yellow // w
            if (w + h) * 2 + 4 == brown:
                print(w, h)
                if w >= h:
                    answer.append(w+2)
                    answer.append(h+2)

    return answer