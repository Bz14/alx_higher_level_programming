#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    res_1 = filter(lambda x: x not in set_1, set_2)
    res_2 = filter(lambda x: x not in set_2, set_1)
    return list(res_1) + list(res_2)
