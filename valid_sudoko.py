# valid_sudoko.py
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        self.board = board
        if not self.check_rows():
            return False
        if not self.check_columns():
            return False
        if not self.check_boxes():
            return False
        return True
    
    def check_rows(self):
        for row in self.board:
            unique = [x for x in row if x != "."]
            if len(unique) != len(set(unique)):
                print("Dumplicate found in {}.".format(row))
                return False
            for value in row:
                if not self.valid_cell(value):
                    return False
        return True

    def check_columns(self):
        for x in range(9):
            column = []
            for y in range(9):
                column.append(self.board[y][x])
            # print(column)
            unique = [x for x in column if x != "."]
            if len(unique) != len(set(unique)):
                print("Dumplicate found in {}.".format(column))
                return False
        return True
            
    def check_boxes(self):
        for x in range(0, 6, 3):
            for y in range(0, 6, 3):
                if not self.check_square(x, y):
                    return False
        return True

            
    def check_square(self, xstart, ystart):
        square = []
        for x in range(xstart, xstart + 3):
            for y in range(ystart, ystart + 3):
                square.append(self.board[x][y])
            unique = [x for x in square if x != "."]
            if len(unique) != len(set(unique)):
                print("Dumplicate found in {}.".format(square))
                return False
        return True
            
    def valid_cell(self, value):
        if value == ".":
            return True
        try:
            number = int(value)
        except TypeError:
            print("Not an integer castable string.")
            return False
        if 1 <= number <= 9:
            return True
        else:
            print("Out of Range.")
            return False
        
x = Solution()

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(x.isValidSudoku(board))

board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(x.isValidSudoku(board))

board = [["8","3","8",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(x.isValidSudoku(board))

board = [
 [".",".","4",".",".",".","6","3","."],
 [".",".",".",".",".",".",".",".","."],
 ["5",".",".",".",".",".",".","9","."],
 [".",".",".","5","6",".",".",".","."],
 ["4",".","3",".",".",".",".",".","1"],
 [".",".",".","7",".",".",".",".","."],
 [".",".",".","5",".",".",".",".","."],
 [".",".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".",".","."]]

print(x.isValidSudoku(board))
