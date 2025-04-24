# https://leetcode.com/problems/length-of-last-word
# Time Complexity O(N)
# Space Complexity O(1)
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Intuition: we start in the reverse order and we keep the
        word count, if we get space and word count =0 that means
        there are spaces at the end of the string, else when we get
        chars then we just increment the word cnt
        Once we get space again (when word count !=0) then we return
        the word count that will be the length of the last word.
        """

        wordCnt = 0

        for i in range(len(s)-1, -1, -1):
            if s[i] == " ":
                if wordCnt == 0:
                    continue
                else:
                    return wordCnt
            else:
                wordCnt +=1

        return wordCnt