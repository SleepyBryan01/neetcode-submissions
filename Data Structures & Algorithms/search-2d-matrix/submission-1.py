class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, col = len(matrix), len(matrix[0])
        top, btm = 0, rows - 1 

        while top <= btm: #shift matrix big pointer 
            row = (top + btm)//2 #calibrate  row
            if target < matrix[row][0]: 
                btm = row - 1
            elif target > matrix[row][-1]: 
                top = row + 1  
            else: 
                break
        
        if not (top <= btm): 
            return False 
        
        l, r = 0 , col - 1 
        row = (top + btm) // 2
        while l <= r: 
            m = (l+r)//2 
            if target > matrix[row][m]: 
                l = m+1 
            elif target < matrix[row][m]: 
                r = m-1 
            else:
                return True 
        
        return False 
             



        