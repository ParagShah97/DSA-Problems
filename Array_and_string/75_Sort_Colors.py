# https://leetcode.com/problems/sort-colors
# Time Complexity: O(N)
# Space Complexity: O(1)

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:

        """
        Intuition:
        This is dutch flag algo question.
        We will take 3 pointer zero_ptr start from 0th index, two_ptr start from last.
        itr start from 0 till <= two_ptr
        The main idea is nums[itr] == 0 then we swap itr and zero_ptr value and move both
        zero_ptr and itr by +1.
        But if nums[itr] == 2 then we swap itr and two_ptr value and only move two_ptr 
        by -1.
        Else move itr by +1 (this is the case of when nums[itr]==1) 
        """
        zero_ptr = 0
        two_ptr =len(nums)-1
        itr = 0

        def swap(i,j):
            temp=nums[i]
            nums[i] = nums[j]
            nums[j]=temp

        while itr <= two_ptr:
            if nums[itr] == 0:
                swap(zero_ptr, itr)
                zero_ptr +=1
                itr+=1

            elif nums[itr]==2:
                swap(two_ptr, itr)
                two_ptr-=1
            else:
                itr+=1      