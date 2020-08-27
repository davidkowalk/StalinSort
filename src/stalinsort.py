def sort(list, sort_min_max = False):

    """
    Takes a list and eliminates all items that are out of order.
    set sort_min_max = True to sort min. value to the front and max. value to the back before applying stalin's superior method of creating order.
    """

    if sort_min_max:
        list = __sort_min_max__(list)


    list_len = len(list)
    i = 1

    while i < list_len-1:
        if not list[i-1]<list[i]<list[i+1]:
            del list[i]
            list_len -= 1
        else:
            i += 1

    if not list[-1] > list[-2]:
        del list[-1]

    return list


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
