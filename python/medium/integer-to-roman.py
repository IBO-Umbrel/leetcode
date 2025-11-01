# medium (but I bilive this one should be hard difficulty!) (https://leetcode.com/problems/integer-to-roman/description/)



# possible combination table:
# V, X, I
# L, C, X
# D, M, C



class Solution:
    def range(self, a: int, b: int, num: int):
        return num >= a and num <= b
    def intToRoman(self, num: int) -> str:
        if num == 0: #======================#
            return ""                       #
        if num <= 3:                        #
            return "I" * num                #
        if num == 4:                        #
            return "IV"                     #========== numbers between 0 and 9
        if self.range(5, 8, num):           #
            return "V" + ((num - 5) * "I")  #
        if num == 9:                        #
            return "IX" #===================#
        if self.range(10, 39, num): #===========================================================#
            return "X" * (num // 10) + self.intToRoman(num % ((num // 10)*10))                  #
        if self.range(40, 49, num):                                                             #
            return "XL" + self.intToRoman(num % 40)                                             #
        if self.range(50, 89, num):                                                             #========== numbers between 10 and 99
            return "L" + ("X" * ((num // 10) - 5)) + self.intToRoman(num % ((num // 10)*10))    #
        if self.range(90, 99, num):                                                             #
            return "XC" + self.intToRoman(num % 90) #===========================================#
        if self.range(100, 399, num): #=============================================================#
            return "C" * (num // 100) + self.intToRoman(num % ((num // 100)*100))                   #
        if self.range(400, 499, num):                                                               #
            return "CD" + self.intToRoman(num % 400)                                                #
        if self.range(500, 899, num):                                                               #========== numbers between 100 and 999
            return "D" + ("C" * ((num // 100) - 5)) + self.intToRoman(num % ((num // 100)*100))     #
        if self.range(900, 999, num):                                                               #
            return "CM" + self.intToRoman(num % 900) #==============================================#
        
        return "M" * (num // 1000) + self.intToRoman(num % 1000) #=============================================== numbers between 1000 and 3999



# running tests here:
print(Solution().intToRoman(3749))
print(Solution().intToRoman(3749) == "MMMDCCXLIX")




# version 1
# class Solution:
#     def intToRoman(self, num: int) -> str:
#         if num == 0:
#             return ""
#         if num < 5:
#             return "I" * num
#         if num < 10:
#             return "V" * (num // 5) + self.intToRoman(num % 5)
#         if num < 50:
#             return "X" * (num // 10) + self.intToRoman(num % 10)
#         if num < 100:
#             return "L" * (num // 50) + self.intToRoman(num % 50)
#         if num < 500:
#             return "C" * (num // 100) + self.intToRoman(num % 100)
#         if num < 1000:
#             return "D" * (num // 500) + self.intToRoman(num % 500)
#         return "M" * (num // 1000) + self.intToRoman(num % 1000)