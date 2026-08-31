class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowHash = {}
        columnHash = {}
        gridHash = {}


        

        rows, cols = len(board), len(board[0])
        b =0
        for r in range(rows):
            columnHash = {}
            rowHash = {}
            
            a =0
            
            for c in range(cols):

                if board[r][c] != "." and board[r][c] in columnHash:
                    return False
                columnHash[board[r][c]] = 1
                if board[c][r] != "."  and board[c][r] in rowHash:
                    return False
                rowHash[board[c][r]] = 1

                if board[r][c] != "." and board[r][c] in gridHash:
                    return False

                gridIndex = f"{a}{b}"
                if gridIndex not in gridHash:
                    gridHash[gridIndex] = {}

                if board[r][c] != "." and board[r][c] in gridHash[gridIndex]:
                    return False
               
                gridHash[gridIndex][board[r][c]] = 1
                #print(f"r={r} c={c} g={a} b={b}  | cell[r][c]={board[r][c]!r} cell[c][r]={board[c][r]!r} |  (c+1)%3={(c + 1) % 3} | colH={sorted(columnHash)} rowH={sorted(rowHash)} gridH={sorted(gridHash)} | a={a} b={b}")
                if (c+1)%3 == 0:
                    a+=1
            if (r+1)%3 == 0:
                b+=1


        return True