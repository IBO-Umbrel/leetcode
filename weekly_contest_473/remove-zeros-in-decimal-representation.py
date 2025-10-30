class Solution:
    def removeZeros(self, n: int) -> int:
        result = ""
        for snum in str(n):
            if snum != "0":
                result += snum
        return int(result)