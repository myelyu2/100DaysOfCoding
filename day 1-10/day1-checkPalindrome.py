"""
Given the string, check if it is a palindrome.
"""

def solution(inputString):
    if (inputString == inputString[::-1]):
        return True
    else:
        return False