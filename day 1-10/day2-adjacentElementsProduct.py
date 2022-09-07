"""
Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.
"""

def solution(inputArray):
    max = -999
    for x, y in zip(inputArray, inputArray[1:]):
        if x * y > max:
            max = x*y
    return max
