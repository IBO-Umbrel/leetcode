# medium (https://leetcode.com/problems/reverse-integer/)


class Solution:
    def reverse(self, x: int) -> int:
        reversed_x = str(x)[::-1]
        reversed_x = reversed_x.replace('-', '')
        reversed_x = int(reversed_x)

        if reversed_x > (2**31) - 1 or reversed_x < -(2**31):
            return 0
        if x < 0: 
            return -reversed_x
        return reversed_x


print(Solution().reverse(1534236469))