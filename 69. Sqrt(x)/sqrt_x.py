"""
https://leetcode.com/problems/sqrtx/
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.
"""


def my_sqrt(x):
    if x <= 1:
        return x
    left, right = 0, x
    while left < right:
        mid = (left + right) >> 1
        squared_mid = mid * mid
        if squared_mid <= x < (mid + 1) * (mid + 1):
            return mid
        if squared_mid > x:
            right = mid
        else:
            left = mid
