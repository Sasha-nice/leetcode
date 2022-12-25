"""
https://leetcode.com/problems/median-of-two-sorted-arrays/

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Submission beats 99.84% runtime.
"""


def find_median_sorted_arrays(nums1, nums2):
    len_1 = len(nums1)
    len_2 = len(nums2)
    sum_len = len_2 + len_1
    i_1, i_2 = 0, 0
    d = sum_len >> 1
    for i in range(d + 1):
        if i == d:
            try:
                f = value
            except UnboundLocalError:
                pass
        if i_1 >= len_1:
            value = nums2[i_2]
            i_2 += 1
        elif i_2 >= len_2:
            value = nums1[i_1]
            i_1 += 1
        else:
            if nums2[i_2] < nums1[i_1]:
                value = nums2[i_2]
                i_2 += 1
            else:
                value = nums1[i_1]
                i_1 += 1
    if sum_len % 2:
        return value
    else:
        return float(value + f) / 2