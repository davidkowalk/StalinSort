def __sort_min_max__(list):
    """
    Sorts minimum to the beginning and the maximum to the end of the list.
    """

    min = list[0]
    min_i = 0
    max = list[0]
    max_i = 0

    for i in range(len(list)):
        el = list[i]

        if el < min:
            min = el
            min_i = i
        elif el > max:
            max = el
            max_i = i

    del list[min_i]
    del list[max_i]

    return [min]+list+[max]
