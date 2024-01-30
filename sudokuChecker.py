from typing import List


class Solution:
   def isValidSudoku(board: List[List[str]]) -> str:
      # Check rows
      for i in range(9):
         if not is_valid_group(board[i]):
            return False   
      # Check columns
      for j in range(9):
         if not is_valid_group([board[i][j] for i in range(9)]):
            return False
      # Check 3x3 subgrids
      for i in range(0, 9, 3):
         for j in range(0, 9, 3):
            if not is_valid_group([board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]):
                  return False
      return True 
   
def is_valid_group(group):
   seen = set()
   for num in group:
      if num != ".":
         if num in seen:
               return False
         seen.add(num)
   return True
# Pseudocode
board = [
["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

board2 = [
 ["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
def get_sudoku(): return board
# print("board:" + str(Solution.isValidSudoku(board)))
# print("board2:" + str(Solution.isValidSudoku(board2)))


# Loop over all sublist in Lists
# Loop all List items "N"
#       Compare with N further items 
#           return False if element exist
#       Loop all list same item index only
#           return False if item match
#       Loop further Neighbors  from m[x, y] - >
#          neighbor[x] is all within quadrant-range neighbor <> item[x] 
#             if multiplo de 3            
#          neighbor[y] is item[y] 

