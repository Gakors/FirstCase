def max_odd(array):
    maxodd = None
    for i in range(len(array)):
        if type(array[i]) in (int, float):
            if array[i] % 2 == 1 and (maxodd is None or array[i] > maxodd):
                maxodd = int(array[i])
    return maxodd


print(max_odd([1, 2, 3, 4, 4]))
print(max_odd([21.0, 2, 3, 4, 4]))
print(max_odd(['ololo', 2, 3, 4, [1, 2], None]))
print(max_odd(['ololo', 'fufufu']))
print(max_odd([2, 2, 4]))