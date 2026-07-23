class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #first we will create sets for all the rows, columns, and the 3*3 boxes
        #we will use defaultdict(set) as it will create a new set mapped to the indice
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9) :
            for c in range(9) :
                if (board[r][c]==".") :
                    continue
                elif (board[r][c] in rows[r] or
                 board[r][c] in cols[c] or
                 board[r][c] in boxes[(r//3, c//3)]):
                    return False
                else :
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    boxes[(r//3, c//3)].add(board[r][c])
        return True


# to add to the set we use .add() not the = cuz this replace the set with the new value ,
# exp : rows[0].add("5") -> rows[0] becomes {"5"}, rows[0].add("3") -> rows[0] is now {"5", "3"}
# rows[0] = "5"       : rows[0] becomes "5"

# boxes[(r//3, c//3)] maps any element of the board to its corresponding box, so it will be compared to elements of the same box, 
# by using the composed key (r//3, c//3) we assigned each box a unique key , which is either (0,0) (0,1) (1,1) .... 


        

        


                    
                
        