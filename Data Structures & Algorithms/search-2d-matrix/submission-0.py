class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        left = 0
        right = len(matrix)*len(matrix[0])-1

        while left<=right :
            m = left + (right-left)//2

            row = m//len(matrix[0])
            column = m%len(matrix[0])

            if matrix[row][column] == target :
                return True
            elif matrix[row][column]<target :
                left = m + 1
            else : 
                right = m -1
        return False

             
        