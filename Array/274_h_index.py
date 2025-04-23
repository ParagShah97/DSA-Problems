# https://leetcode.com/problems/h-index/description/
# Time Complexity: O(N)
# Space Complexity: O(N)
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
        Intuition:
        Brute Force:
        Here we can start from h = 0 to n (len of citation).
        for every h value we will iterate from 0th to n-1 index and check
        if the citation[i] > h value of h number of times then we can break and
        check for the next greater value.
        Here we will return the greatest value of H that work on the above algo.

        Improved approach:
        Here we will keep an array temp of size = citation size+1.
        We will iterate over the citations array and increment the temp array
        index value against the citation array value.
        Later we can iterate in reverse on temp and add the values till value
        sum > index, as soon we get the sum >= index we can return index.
        """
        # Temp will store the count of citation e.g. citation[i] =2, then 
        # temp[2] += 1.
        temp = [0]*(len(citations)+1)

        # Iterate over the citation values
        for i in citations:
            # if the value greater than len(citation) then inc the last idx ele.
            if i > len(citations):
                i = len(citations)
            temp[i] += 1
            # temp[min(i,len(citation))] += 1  # this will work too

        # Count the citation, once the value go above the index that means
        # we get the citattion count atleast number of papers.
        cite = 0
        for i in range(len(temp)-1, -1, -1):
            cite += temp[i]
            if i <= cite:
                return i
        return -1   # not required just for fail safe. 

        #  O(Nlog(N))
        # citations.sort(reverse=True)
        # h = 0
        # for i, c in enumerate(citations):
        #     if c >= i + 1:
        #         h = i + 1
        #     else:
        #         break
        # return h