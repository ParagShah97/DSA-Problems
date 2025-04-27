# https://leetcode.com/problems/group-anagrams
# Time Complexity: O(N*k)
# Space Complexity: O(26*N)
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Intution: 
        We can keep the res dict values as lists.
        Iterate over all the string from str, and keep the cnt of size 26, for every char
        in the s (current word) increment the count at index of alphabet.
        Use the count array as key (make it tuple) and value add the curret word.
        At last return list of all the values.
        '''
        res = defaultdict(list)

        for s in strs:
            count = [0]*26

            for c in s:
                count[ord(c)-ord('a')] +=1

            res[tuple(count)].append(s)

        # print(res.values())
        return list(res.values())
        