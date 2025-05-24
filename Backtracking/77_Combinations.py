# https://leetcode.com/problems/combinations
# Time Complexity: O(C(n, k) × k)
# Space Complexity: O(C(n, k) × k)
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        Intuition:
        We can use the concept of backtracking. For each recursion we pass
        the index and the current array.
        Base case: if the len of current array == k then save a copy in ans.
        In every recursion, we will iterate over current index to n+1 and
        add the digit and call next recursion then pop out (backtracking).
        At last return the list.
        """
        # Let's calculate how many combination possible from n & k.
        # num = 1
        # deno =1
        # for i in range(k):
        #     num *= n-i
        #     deno *= k-i

        # total = (num // deno)
        ans = []
        
        def backtrack(idx, cur_comb):
            # if len(ans) == total:
            #     return
            if len(cur_comb) == k:
                ans.append(cur_comb.copy())
                return
            
            for digit in range(idx, n+1):
                cur_comb.append(digit)
                backtrack(digit+1, cur_comb)
                cur_comb.pop()
        backtrack(1, [])
        return ans