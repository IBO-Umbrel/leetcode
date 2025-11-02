# medium (https://leetcode.com/problems/count-unguarded-cells-in-the-grid/)


from typing import List


class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        total_cells = m * n
        walls_set = {tuple(w) for w in walls}
        gaurds_set = {tuple(g) for g in guards}
        guarded_cells = set()

        for grow, gcol in guards:
            # right
            for col in range(gcol+1, n):
                if (grow, col) in walls_set or (grow, col) in gaurds_set:
                    break
                guarded_cells.add((grow, col))
            # left
            for col in range(gcol-1, -1, -1):
                if (grow, col) in walls_set or (grow, col) in gaurds_set:
                    break
                guarded_cells.add((grow, col))
            # bottom
            for row in range(grow+1, m):
                if (row, gcol) in walls_set or (row, gcol) in gaurds_set:
                    break
                guarded_cells.add((row, gcol))
            # top
            for row in range(grow-1, -1, -1):
                if (row, gcol) in walls_set or (row, gcol) in gaurds_set:
                    break
                guarded_cells.add((row, gcol))
    
        return total_cells - len(walls_set) - len(gaurds_set) - len(guarded_cells)



# running tests here:
m = 4
n = 6
guards = [[0,0],[1,1],[2,3]]
walls = [[0,1],[2,2],[1,4]]


print(Solution().countUnguarded(m, n, guards, walls))





# old version
# class Solution:
#     def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
#         unguarded_cells = m * n
#         guarded_cells = []

#         for i in range(m):
#             for j in range(n):
#                 cell = [i, j]
#                 if cell in guards or cell in walls:
#                     unguarded_cells -= 1
#                 if cell in guards:
#                     # right
#                     if j < n-1:
#                         for r in range(j+1, n):
#                             current_cell = [i, r]
#                             if current_cell in walls or current_cell in guards:
#                                 break
#                             if not current_cell in guarded_cells:
#                                 unguarded_cells -= 1
#                             guarded_cells.append(current_cell)
#                     # left
#                     for l in range(j-1, -1, -1):
#                         current_cell = [i, l]
#                         if current_cell in walls or current_cell in guards:
#                             break
#                         if not current_cell in guarded_cells:
#                             unguarded_cells -= 1
#                         guarded_cells.append(current_cell)
#                     # bottom
#                     if i < m-1:
#                         for b in range(i+1, m):
#                             current_cell = [b, j]
#                             if current_cell in walls or current_cell in guards:
#                                 break
#                             if not current_cell in guarded_cells:
#                                 unguarded_cells -= 1
#                             guarded_cells.append(current_cell)
#                     # top
#                     for t in range(i-1, -1, -1):
#                         current_cell = [t, j]
#                         if current_cell in walls or current_cell in guards:
#                             break
#                         if not current_cell in guarded_cells:
#                             unguarded_cells -= 1
#                         guarded_cells.append(current_cell)

#         return unguarded_cells