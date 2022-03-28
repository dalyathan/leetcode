class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        num_rows= len(grid)
        num_cols= len(grid[0])
        for region in range(min(num_rows//2,num_cols//2)):
            for i in range(k % ( 2 * (num_cols - 2*region + num_rows - 2*region) - 4)):
                empty= grid[region][region] 
                for row_num in range(region+1, num_rows - region):
                    grid[row_num][region], empty = empty, grid[row_num][region]
                for col_num in range(region+1, num_cols - region):
                    grid[num_rows-1-region][col_num], empty = empty, grid[num_rows-1-region][col_num]
                for row_num in range(num_rows - 1 - region - 1, region - 1, -1):
                    grid[row_num][num_cols-1-region], empty = empty, grid[row_num][num_cols-1-region]
                for col_num in range(num_cols - 1 - region - 1, region - 1, -1):
                    grid[region][col_num], empty = empty, grid[region][col_num]
        return grid
                