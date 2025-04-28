# https://leetcode.com/problems/happy-number
# Time Complexity O(k)
# Space Complexity O(1)
class Solution:
    """
    Intuition:
    I created a helper function which will to calculate the digit sq sum.
    We call the helper funcition from the infinite loop, every iteration
    we call the check if the sq sum == 1 then return True, or
    1. If it already seen before (we can check from the set()) False
    2. If not seen add to the set and check for the next number.
    """
    def isHappy(self, n: int) -> bool:
        repeatset = set()

        def calculateAns(num):
            cal = 0
            while num > 0:
                d = num % 10
                cal+=d**2
                num = num//10
            return cal
        cur = n
        while True:
            cur = calculateAns(cur)
            if cur in repeatset:
                return False
            if cur == 1:
                return True
            repeatset.add(cur)
        
        return False