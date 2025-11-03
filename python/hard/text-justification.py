# hard (https://leetcode.com/problems/text-justification/)


from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        curr = []
        chars = 0
        for word in words:
            if chars + len(curr) + len(word) > maxWidth:
                if len(curr) == 1:
                    result.append(curr[0] + " " * (maxWidth - len(curr[0])))
                else:
                    empty_spaces = maxWidth - chars
                    even_spaces = empty_spaces // (len(curr) - 1)
                    extra_spaces = empty_spaces % (len(curr) - 1)
                    line = ""

                    for index in range(len(curr)):
                        line += curr[index]

                        # adding spaces
                        if index < len(curr) - 1:
                            line += " " * (even_spaces + (1 if index < extra_spaces else 0))
                        
                    result.append(line)
                curr = []
                chars = 0
            curr.append(word)
            chars += len(word)
        
        last_line = " ".join(curr)
        last_line += " " * (maxWidth - len(last_line))
        result.append(last_line)
        
        return result
    


# running tests here:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
print(Solution().fullJustify(words, maxWidth))