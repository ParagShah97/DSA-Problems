# Problem https://leetcode.com/problems/merge-intervals/
# Time Complexity: O(Nlog(N))
# Space Complexity: O(N)
from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        Intuition:
        If we sort the intervals on the basis of start time, we can get the list of
        intervals in a order.
        We check if final list(ans) is empty or a seperate interval:
        (nextInt[0] > prevAddedInt[1]) then we can add the interval normally.
        Else: We have to merge the intervals for prevAddedInterval the end range is 
        updated to max(prevAddedInterval[1], nextInterval[1])
        '''
        ans = []
        intervals.sort()
        for i in intervals:
            # If array is empty
            # or, previously added interval end time less than next interval start.
            if not ans or ans[-1][1] < i[0]:
                ans.append(i)
            # Else, we have to merge the intervals, by changing the end time of
            # already addded interval.
            else:
                ans[-1][1] = max(ans[-1][1], i[1])
            
        return ans


def main():
    test_cases = [
        [[1,3],[2,6],[8,10],[15,18]],
        [[1,4],[4,5]]
    ]
    
    solution = Solution()
    for intervals in test_cases:
        print(f"Input: {intervals}")
        result = solution.merge(intervals)
        print(f"Output: {result}\n")
        
if __name__ == "__main__":
    main()
