# hard (https://leetcode.com/problems/valid-number/description/)


import re
class Solution: 
    def isNumber(self, s: str) -> bool:
        return bool(re.fullmatch(r"[+-]?((([0-9]+[.]?[0-9]*)|([.][0-9]+))([eE][+-]?[0-9]+)?)", s))