class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #first we will create sets for all the rows, columns, and the 3*3 boxes
        #we will use defaultdict(set) as it will create a new set mapped to the indice
        
        """
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
        """


# to add to the set we use .add() not the = cuz this replace the set with the new value ,
# exp : rows[0].add("5") -> rows[0] becomes {"5"}, rows[0].add("3") -> rows[0] is now {"5", "3"}
# rows[0] = "5"       : rows[0] becomes "5"

# boxes[(r//3, c//3)] maps any element of the board to its corresponding box, so it will be compared to elements of the same box, 
# by using the composed key (r//3, c//3) we assigned each box a unique key , which is either (0,0) (0,1) (1,1) .... 
# but this first solution is O(n*2) time and space complexity, we will try another with just O(n) space complexity

# the Bitmask solution

        rows = [0]*9
        cols = [0]*9
        boxes = [0]*9

        for r in range(9) :
            for c in range(9) :
                if board[r][c] == "." :
                    continue 
                val = int(board[r][c]) - 1 # we substract 1 cuz the 1<<val operation sets the bit 1 in the val+1 position which bring us back to the desired position of int(board[r][c])
                mask = 1 << val 
                # 1 in binary is 000000001 , and 1<< val is shifting left by val position , means 1<<5 is 000100000
                if (mask & rows[r]) or (mask & cols[c]) or (mask & boxes[(r//3)*3+(c//3)]) :  # in Java if ((rows[r] & mask) != 0)
                    return False
                else :
                    rows[r] |= mask # same as rows[r] = rows[r] | mask : it is the Or operation that sets a bit to 1 if EITHER bit is 1, so it adds the
                    cols[c] |= mask
                    boxes[(r//3)*3+c//3] |= mask 
        return True
                
# Correct: unique box index 0-8 : box_index = (r // 3) * 3 + c // 3





        

        


                    
                
        