# https://leetcode.com/problems/reorganize-string
# Time Complecity: O(Nlog(N))
# Space Complecity: O(N)
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        """
        Intuition:
        First we can create the counter dictionary.
        Then convert the dict into a list [(-freq, character)] then heapify it.
        Then iterate till the heap is not empty.

        Every iteration pop 2 elements from the heap, and append to ans.
        then increment the value of freq as we stored the freq in * -1 for
        max heap.
        If the freq not equal 0 then push back to the heap.
        Note: Here a case when there is only one element left in the heap in that
        case we check if the freq of that element is > 1 then return "".
        Else append the character at back of ans.

        At last return the ans string.
        """
        cnt_map = {}
        for c in s:
            cnt_map[c] = cnt_map.get(c, 0) + 1
        # Max Heap
        cnt_heap = []
        
        for k,v in cnt_map.items():
            cnt_heap.append((-v,k))
        
        heapq.heapify(cnt_heap)
        ans = []
        while cnt_heap:
            if len(cnt_heap) ==1:
                if cnt_heap[0][0] < -1:
                    return ""
                else:
                    ans.append(cnt_heap[0][1])
                    break
            # print(cnt_heap)
            first, f_al = heapq.heappop(cnt_heap)
            second, s_al = heapq.heappop(cnt_heap)
            ans.append(f_al)
            ans.append(s_al)
            first+=1
            second+=1

            if first != 0:
                heapq.heappush(cnt_heap, (first, f_al))
            if second != 0:
                heapq.heappush(cnt_heap, (second, s_al))


        return "".join(ans)      