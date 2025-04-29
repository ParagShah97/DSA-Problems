# Time Complexity O(N)
# Space Complexity O(N)
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        Brute force:
        Here we can take a set and sort it.
        we take curr and ans (largest) variable starts with 1
        Now iterate from i -> 0 to n-1 if nums[i] == nums[i+1]-1 then increase the curr 
        count and update ans if it's greater than already had value.
        else we make curr Cnt = 1, at last we will return ans.

        Approach 2: Optimal
        Here consider <--- 1,2,3,4---100---200--> is a number line,
        The idea is after converting the num list to set, we check 
        if cur num is start of the list or not (by checking num-1 
        present in set if not then yes).

        So, if cur element is start of list then we check in loop for
        i+1 is present in set if yes increment the lenght and check of 
        next element.
        At last check the max len and return max len.
        '''
        # Optimized O(n)
        # If array is empty
        if len(nums) == 0:
            return 0
        # Use a set to store all the element of nums
        numSet = set(nums)  #O(N)
        ans = 0
        # Iterate over all the elements
        for i in numSet:
            # If there is not i-1 element present then the element can be start
            # of a sequence, can be not always.
            if (i-1) not in numSet:
                # Will use lenght for counting and incrementing as well.
                length = 0
                while (i+length) in numSet:
                    length += 1
                # Check for if the length is global max or not.
                ans=max(ans, length)
        
        return ans



        