"""
https://leetcode.com/problems/palindrome-number/
Given an integer x, return true if x is a palindrome, and false otherwise.
"""


def is_palindrome(x):
    input_string = str(x)
    return input_string == input_string[::-1]