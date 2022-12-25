"""
https://leetcode.com/problems/single-number/

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
"""
from functools import reduce


def single_number(nums):
    return reduce(lambda x, y: x ^ y, nums)
