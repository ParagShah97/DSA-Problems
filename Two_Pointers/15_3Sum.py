# https://leetcode.com/problems/3sum
# Time Complexity O(Nlog(N)) + O(N^2) = O(N^2) 
# Space Complexity O(N^2) (For return data) else O(1)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Intuition:
        First we can sort the nums array, so we can apply 2 pointer apporach easily.
        We iterate from 0 to n, and for each index,
        {Corner case, when i>0 (not the first index), and i==i-1 index ele then we
        continue to next ith value.}
        we keep left and right pointer left in 1+currentIndex and right is last index.
        Inside the iteraton we loop till l<r and calculate sum of i,l,r index ele.
        If sum < 0, we move left ->
        If sum > 0, we move right <-

        if we found sum =0 then we add that to ans list and move left (->),
        Also, we check if the next lth index == previous l index then we move
        left (->) in a while loop.
        """
        # Let's first sort the array
        nums.sort()
        ans = []
        for i in range(len(nums)):
            # first we check the current index > 0 and current element
            # not equal to previous else go to next.
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1

            while l<r:
                sum3 = nums[i]+nums[l]+nums[r]
                # here we know that the array is sorted.
                # if sum < 0 that mean we need to move l pointer to the left.
                if sum3 < 0:
                    l += 1
                # if sum > 0 that mean we need to move r pointer to the right.
                elif sum3> 0:                    
                    r -= 1
                # if sum = 0 that, we can add the i, l, r indexed array values to the ans.
                else:
                    ans.append([nums[i],nums[l],nums[r]])
                    # just increment the l to the right.
                    l += 1
                    # Now we check if adjecent to l pointer are the values are same, if so then,
                    # 
                    while nums[l] == nums[l-1] and l<r:
                        l += 1
        return ans