from typing import List
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
	# starting form (0,0) so add it to queue.
        length,queue = len(grid), deque([(0,0,1)])
	# Array with all 8 directions
        directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]

# (0,0) and (n-1,n-1) must be 0 for a clear path.
        if grid[0][0] == 1 or grid[length-1][length-1] == 1:
            return -1
        grid[0][0] = 1    # marking as visited, since already in queue
        
        while queue:
            x,y,dist = queue.popleft()
            print(x,y, grid[x][y], dist)

            if (x,y) == (length-1,length-1):    # reached bottom-right cell, so return distance
                return dist

            for newX,newY in directions:  # traversing in all 8 directions
                i,j = x+newX, y+newY

                
                if 0<= i <length and 0<= j <length and grid[i][j] == 0:  # making sure (i,j) is in grid
                    queue.append((i,j,dist+1))
                    grid[i][j] = 1
        return -1

if __name__ == "__main__":
    print(Solution().shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]))
