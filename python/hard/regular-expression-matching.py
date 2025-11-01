# hard (https://leetcode.com/problems/regular-expression-matching/)


import re


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return bool(re.fullmatch(p, s))
    

print(Solution().isMatch("aa", "a"))