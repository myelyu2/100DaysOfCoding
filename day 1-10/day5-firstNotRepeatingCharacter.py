"""
Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.

"""

def solution(s):
    d = {}
    for c in s:
        d[c] = 1 if c not in d else d[c] + 1
        
    for c in s:
        if d[c] == 1: return c
    
    return "_"