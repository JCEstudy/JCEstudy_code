def solution(answers):
    per1 = [1, 2, 3, 4, 5]
    per2 = [2, 1, 2, 3, 2, 4, 2, 5]
    per3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    count = [0, 0, 0]

    for i, answer in enumerate(answers):

        if answer == per1[i % len(per1)]:
            count[0] += 1

        if answer == per2[i % len(per2)]:
            count[1] += 1

        if answer == per3[i % len(per3)]:
            count[2] += 1

    max_value = max(count)

    result = []

    for i, value in enumerate(count):
        if value == max_value:
            result.append(i + 1)

    return result