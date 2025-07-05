# https://leetcode.com/problems/reverse-integer
# Time Complexity: O(N)
# Space Complexity: O(1)
import math


class Solution:
    """
    Intuition:
    Here we leverage the idea of reversing the number by mod (last digit) and
    integer divinding to get one less digit number, and creating reverse number
    by multiplying 10 to previous digits and adding current digit.

    In Between we need to check 2 condition that if current number is greater
    than MAX int size without last digit. or ans equal to MAX without last digit.
    and last digit greater or equal MAX last digit.
    Same case for MIN as well.
    For both the case return 0.
    """
    def reverse(self, x: int) -> int:
        MIN= -2147483648 # -2^31
        MAX= 2147483647 # 2^31-1

        ans = 0
        while x:
            last_digit = int(math.fmod(x,10))
            x=int(x/10)

            if (ans > MAX // 10 or (ans == MAX // 10 and last_digit >= MAX % 10)):
                return 0
            if (ans < MIN // 10 or (ans == MIN // 10 and last_digit <= MIN % 10)):
                return 0
            ans= (ans*10) + last_digit
        return ans