# Problem URL: https://leetcode.com/problems/surrounded-regions/

# Time Complexity: O(M*N)
# Space Complexity: O(M*N)
from typing import List
class Solution:
    def solve(self, b: List[List[str]]) -> None:
        '''
        Intuition:
        Here we can think differently, we can start a dfs call from the boudries and mark
        the region which are connected from the boundry to some other character like "#".

        After the dfs call, all the region connetcted from the boundry in some way change
        to "#".

        We can iterate normally and change all the # -> O and unchanged O -> X. As those
        O not  converted to # are not connect to the boundry.
        '''
        ROWS, COLS = len(b), len(b[0])

        def dfs(r,c):
            # If r and c are out of range
            # if b[r,c] == X or b[r,c] == # do nothing.
            if r < 0 or r == ROWS or c <0 or c==COLS or b[r][c] == "X" or b[r][c] == "#":
                return

            # Change the current O to #
            b[r][c] = "#"
            
            # Call dfs in all 4 directions.
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)

        # Iterate only for boundry
        for r in range(ROWS):
            for c in range(COLS):
                if (r == 0 or c==0 or r == ROWS-1 or c == COLS-1) and b[r][c] == "O":
                    dfs(r,c)
        
        # Change unhanged O to X and # to O.
        for r in range(ROWS):
            for c in range(COLS):
                if b[r][c] == "O":
                    b[r][c] = "X"
                if b[r][c] == "#":
                    b[r][c] = "O"
    


def main():
    # Create an instance of Solution
    solution = Solution()

    # Define test boards
    test_board1 = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    test_board2 = [["X"]]
    test_board3 = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","O","X"]]
    
    # Test 1
    print("--- Test 1 ---")
    solution.solve(test_board1)
    for row in test_board1:
        print(" ".join(row))
    
    # Test 2
    print("--- Test 2 ---")
    solution.solve(test_board2)
    for row in test_board2:
        print(" ".join(row))
    
    # Test 3
    print("--- Test 3 ---")
    solution.solve(test_board3)
    for row in test_board3:
        print(" ".join(row))

if __name__ == "__main__":
    main()
