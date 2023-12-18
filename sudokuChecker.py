from typing import List
class Solution:
   def isValidSudoku(board: List[List[str]]) -> str:
      # return False
      for y in range(0,len(board)):
         for x in range(0,len(board[y])-1):
            if board[y][x] == ".":
               continue
            for xcomp in range(x+1,len(board[y])):
               if board[y][xcomp] == ".":
                  continue
               if board[y][xcomp] == board[y][x]:
                  return False
            if y <= len(board[y]) - 1:
               for ycomp in range(y+1,len(board[y])):
                  if board[ycomp][x] == ".":
                     continue
                  if board[ycomp][x] == board[y][x]:
                     return False
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
print("board:" + str(Solution.isValidSudoku(board)))
print("board2:" + str(Solution.isValidSudoku(board2)))

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

