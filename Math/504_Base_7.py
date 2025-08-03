# https://leetcode.com/problems/base-7/
# Time Complexity: O(Log7(n))
# Space Complexity: O(Log7(n))

class Solution:
    def convertToBase7(self, num: int) -> str:
        """
        Inuition:
        There will be 2 cases either the number is positive or negative.
        Initially we check and store if the number is +ve or -ve.
        Then iterate till abs(num) > 0, every time we take modulo by 7 and 
        append the remainder to the list and then divide the num by 7.
        After the loop we check if the number is -ve if yes then we append the - at last

        At last we reverse and return the join string as ans.

        """
        if num == 0:
            return '0'
        isNeg = True if num < 0 else False

        num = abs(num)
        rem = []
        while num > 0:
            remainder = num % 7
            rem.append(str(remainder))
            num = num // 7

        if isNeg:
            rem.append('-')
        rem.reverse()
        return ''.join(rem)