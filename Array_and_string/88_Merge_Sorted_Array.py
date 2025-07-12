# https://leetcode.com/problems/merge-sorted-array
# Time Complexity: O(N)
# Space Complexity: O(1) Optimized | O(N) brute force
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        """
        Intuition:
        Let take 3 pointer x at m-1, z at (m+n)-1 on nums1 | y at n-1 on nums2.
        Will iterate from z till 0.
        If the nums1[x] < nums2[y] then we put nums1[z] = nums2[y] (greater value in last)
        elif nums1[x] > nums2[y] then we put nums1[z] = nums1[x] (greater value in last)
        Here to more condition be like if x reach till zero then assign for 
        all nums1[z]=nums2[y].
        And, if y reach 0 then we can break, as all the previous x values are any ways smaller.
        """
       
        # Optimal
        x = m-1
        y=n-1
        z = (m+n)-1

        while z >= 0:
            if x < 0:
                nums1[z] = nums2[y]
                y-=1
                z-=1
            elif y<0:
                break
            elif nums1[x] <= nums2[y]:
                nums1[z] = nums2[y]
                y-=1
                z-=1
            else:
                nums1[z] = nums1[x]
                z-=1
                x-=1

        """
        Intuition :
        Here use the idea of merge sort merge method, took a temp array a copy of nums1
        and then we iterate till either m or n, and place the smaller element to the nums1
        array.
        """
        # Brute Force
        # # Base case, if first array is empty them put elem from second to first arr.
        # if m == 0:
        #     for i in range(n):
        #         nums1[i] = nums2[i]
        #     return
        # # Base case, if the second array is empty then do nothing just return.
        # if n ==0:
        #     return

        # # Take a temp (copy of nums1)
        # temp = nums1[:]
        # i,j,k=0,0,0

        # # Which ever is smaller m or n those many element are paced in nums1
        # while i<m and j<n:
        #     if temp[i] < nums2[j]:
        #         nums1[k] = temp[i]
        #         i+=1
        #         k+=1
        #     else:
        #         nums1[k] = nums2[j]
        #         j+=1
        #         k+=1
        
        # # Below loops for the remaining elem's for the array.
        # while i<m:
        #     nums1[k]=temp[i]
        #     i+=1
        #     k+=1
        # while j<n:
        #     nums1[k] = nums2[j]
        #     j+=1
        #     k+=1