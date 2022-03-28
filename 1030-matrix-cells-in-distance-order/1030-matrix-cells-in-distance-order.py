class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        radius=1
        cells=[[rCenter,cCenter]]
        dont_terminate= True
        terminate_loop= False
        offsets=[]
        while not terminate_loop:
            offsets= [[radius,0],[-radius,0]]
            xs= range(-radius+1,radius)
            for each in xs:
                offsets.append([each,radius-abs(each)])
                offsets.append([each,-(radius-abs(each))])
            terminate_loop= True
            for offset in offsets:
                cell_row= rCenter + offset[0]
                cell_col= cCenter + offset[1]
                if 0 <=  cell_row < rows and 0 <= cell_col < cols :
                    cells.append([cell_row, cell_col])
                    terminate_loop= False
            radius+=1
        return cells