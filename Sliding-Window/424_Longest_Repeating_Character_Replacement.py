# https://leetcode.com/problems/longest-repeating-character-replacement/
# Time Complexity : O(N)
# Space Complexity: O(N)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Intuition:
        Here we can use sliding window approach.
        Here we need counter dic, max ans, maxF (optional)
        We iterate from right pointer.
        First we check if the ele in dic then inc the current element 
        else assign 1.
        Then, we check if the sub-str length - most freq element from dic
        is greater than K then we, move l to the right and decrement dic value 
        against l.
        Here, sub-str len - most_freq elem means how many other character than
        most freq. for example (AABABAA, here A: 5, B:2, and if k=2 then we can replace
        both B to A and overall sub-str lenght will be 7)
        At last, we update the max ans.
        """

        # Keep the dict to store the count of all the char from s
        dic = {}
        # To store max length of the sub string with k replacement
        ans = 0
        # Most freq element
        maxF = 0
        # For sliding window, left pointer
        l = 0
        # Iterate right pointer from 0th to n index.
        for r in range(len(s)):
            # Initially we add or update the count of rth index char.
            dic[s[r]] = 1+dic.get(s[r], 0)
            # Update the most freq element
            maxF = max(maxF, dic[s[r]])
            # Here, we will check if the substring lenght (r-l+1) - most
            # frequent dict value is greater than k, in that case we need to move the
            # left pointer, and update the dict value, {see intuition}
            while (r-l+1)-maxF > k:
            # while (r-l+1)-max(dic.values()) > k:
                dic[s[l]] -= 1
                l +=1
            # calculate the max sub-str lenght.
            ans = max(ans, (r-l+1))
        
        return ans