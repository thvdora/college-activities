def is_list_permutation(L1, L2):
    if L1 == [] and L2 == []:
        return (None, None, None)
    elif len(L1) != len(L2):
        return False

    count_l1 = {}
    for i in range(len(L1)):
        count_l1[L1[i]] = count_l1.get(L1[i], 0) + 1

    count_l2 = {}
    for i in range(len(L2)):
        count_l2[L2[i]] = count_l2.get(L2[i], 0) + 1

    if count_l1 != count_l2:
        return False

    max_count = 0
    most_element = None
    for j in count_l1.items():
        if j[1] > max_count:
            max_count = j[1]
            most_element = j[0]

    return (most_element, max_count, type(most_element))

print(is_list_permutation( ['a', 'a', 'b'], ['a', 'b']))
print(is_list_permutation( ['a', 'b', 'c'], ['a', 'b', 'c']))
print(is_list_permutation( [], []))