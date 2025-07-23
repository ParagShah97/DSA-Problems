# https://leetcode.com/problems/word-ladder/
# Time Complexity: O(M*N*26) in worst case 26 else unique character in word list.
# Space Complexity: O(N)

from collections import deque
from typing import List


class Solution:
    def ladderLength(self, start: str, end: str, wordList: List[str]) -> int:

        """
        Intuition:
        The main idea is we will do a bfs over all the new words that can be formed
        by replacing a charater and also present in the words list.
        The character that we need to replace in order to make new words can be 
        get from the unique character from the wordList.

        Firts we will have all word list,  (unique words)
        Then we have set of word list.

        Then we will do a BFS (keeping queue, visited set, level).

        Till the queue is not empty, we can iterate and for each cycle we
        will iterate till queue len.
        If the curent word popout from the queue is = end word then return level+1
        else we will replace each word from the current string (replacing words are 
        from all_words list that I formed earlier.)

        If the formed word in word list but not visited already then we add
        the wrods to the queue and vistied set.

        At last we will return 0 as level if we not able to find the end word.
        """

        # Let have all possible characters to replace in start string.
        all_words = list(set([ch for ch in "".join(wordList)]))
        words_set = set(wordList)

        q = deque()
        q.append(start)
        vis = set()
        vis.add(start)
        level = 0
        # Till queue not empty as we are doing BFS
        while q:
            q_len = len(q)
            while q_len > 0:
                cur_str = q.popleft()
                q_len -= 1

                if cur_str == end:
                    return level+1

                for ch in all_words:
                    for i in range(len(cur_str)):
                        nei = list(cur_str)
                        nei[i] = ch
                        nei = "".join(nei)

                        # Now let's check if nei is present in word_list.
                        # And check if nei is already visted.

                        if nei not in vis and nei in words_set:
                            vis.add(nei)
                            q.append(nei)
        
            level += 1
        
        return 0