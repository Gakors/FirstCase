import math


def coincidence(list=None, range=None):
    if list is None or range is None:
        return []
    result = []
    lenlist = len(list)
    i = 0
    while i < lenlist:
        if type(list[i]) in (int, float):
            if math.ceil(list[i]) in range:
                result.append(list[i])
        i+=1
    return result


print(coincidence([1, 2, 3, 4, 5], range(3, 6)))
print(coincidence())
print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)))