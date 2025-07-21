# https://leetcode.com/problems/minimum-moves-to-reach-target-score/
# Time Complexity: O(log target)
# Space Complexity: O(1)
class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        """
        Intuition:
        Here the main idea is to start from the target and make it value till one, in the process
        count the steps to make it 1.
        Base case:
        If the maxDouble == 0 then it is obvious that need target-1 steps (0 steps) to reach the target 1.

        If not then we iterate over a while loop, where maxDouble > 0 and target != 1
        Here we have to check 2 condition:
        If target is even: If yes:
        target//2, increment ans and decremnt maxdouble.
        If no:
        target-=1
        ans+=1

        Now once we exhaust maxDouble and target still > 1 then inc ans count by target-1.

        At last return ans count.
        """
        if maxDoubles == 0:
            # Here, to reach target from it's value to 1 will be target -1.
            return target-1
        ans = 0
        while maxDoubles > 0 and target != 1:
            if target % 2 == 0:
                target //= 2
                ans +=1
                maxDoubles-=1
            else:
                target-=1
                ans+=1
        if target > 1:
            ans+=target-1
        
        return ans