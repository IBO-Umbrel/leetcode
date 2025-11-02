# hard (https://leetcode.com/problems/integer-to-english-words/)


from typing import List


class Solution:
    def helper(self, num: int, belowTwenty: List[str], tens: List[str]) -> str:
        result = ""
        if num == 0:
            return ""
        elif num < 20:
            result += belowTwenty[num] + " "
        elif num < 100:
            result += tens[num // 10] + " "
            result += self.helper(num % 10, belowTwenty, tens)
        else:
            result += belowTwenty[num // 100] + " Hundred "
            result += self.helper(num % 100, belowTwenty, tens)
        return result
    def numberToWords(self, num: int) -> str:

        if num == 0:
            return "Zero"

        belowTwenty = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
            "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]
        result = ""
        i = 0;

        while num > 0:
            if (num % 1000 != 0):
                result = (self.helper(num % 1000, belowTwenty, tens) + thousands[i] + " ") + result
            num //= 1000
            i += 1

        return result.strip()



print(Solution().numberToWords(1234567));