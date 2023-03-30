#!/usr/bin/python3

"""find peak of list of unsorted numbers"""


def find_peak(li):
    """caller function"""
    if li is None or li == []:
        return None

    return peak_helper(li, 0, len(li) - 1)


def peak_helper(li, start, end):
    """helper function"""
    m = int((end - start)/2 + start)

    if m + 1 >= len(li) or li[m + 1] <= li[m]:
        if m - 1 < 0 or li[m - 1] <= li[m]:
            return li[m]
        else:
            return peak_helper(li, 0, m)
    else:
        return peak_helper(li, m + 1, end)
