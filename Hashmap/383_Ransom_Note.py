# https://leetcode.com/problems/ransom-note
# Time Complexity: O(N)
# Space Complexity: O(N)
from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Intuition:
        Check first if len(ransomNote) > len(magazine) return False
        len(ransomNote) == len(magazine) == 1 then if both string are
        same then return True else False.
        Use a hashmap to store the counts of magazine.
        Then Iterate over ransomNote and for each char check if it present
        in the counter or not, if not return False.
        For char is present in cnt and it's count > 0 then reduce count, and
        if it's zere then return False.
        At last return True, (means all the condition is cleared and returned.)
        """
        if len(ransomNote) > len(magazine):
            return False
        elif len(ransomNote) == len(magazine) == 1:
            if magazine == ransomNote:
                return True
            else:
                return False

        cnt = Counter(magazine)

        for ch in ransomNote: #O(N)
            if ch not in cnt: #O(1)
                return False
            else:
                if cnt[ch] > 0:
                    cnt[ch] -= 1
                else:
                    return False
        return True