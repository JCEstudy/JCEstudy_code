def solution(sizes):
    max1, max2 = 0, 0
    for i in sizes:
        i.sort()
        if max1 < i[0]:
            max1 = i[0]
        if max2 < i[1]:
            max2 = i[1]
    return max1 * max2