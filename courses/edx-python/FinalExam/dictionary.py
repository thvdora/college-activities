def uniqueValues(adict):
    if adict == {}:
        return []

    count_values = {}
    for key in adict:
        value = adict[key]
        if value in count_values:
            count_values[value] += 1
        else:
            count_values[value] = 1

    result = []
    for key in adict:
        value = adict[key]
        if count_values[value] == 1:
            result.append(key)
    result.sort()
    return result


print(uniqueValues({1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0}))
