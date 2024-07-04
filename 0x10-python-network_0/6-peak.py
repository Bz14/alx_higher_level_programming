#!/usr/bin/python3
""" Finding peak in unsorted integers """


def find_peak(list_of_integers):
    """ Finding peak number """
    n = len(list_of_integers)
    if n == 0:
        return None
    if n == 1:
        return list_of_integers[0]
    if n == 2:
        return max(list_of_integers[0], list_of_integers[1])
    l = 0
    r = n - 1
    nums = list_of_integers
    while l <= r:
        mid = (l + r) // 2
        if ((mid == 0 or nums[mid - 1] <= nums[mid])
            and (mid == n - 1 or nums[mid + 1] <= nums[mid])):
            return nums[mid]
        elif mid > 0 and nums[mid + 1] > nums[mid]:
            l = mid + 1
        else:
            r = mid
    return None
