def bruteValidSudoku(board: list[list[int]]) -> bool:
    seen_values = []
    for row in range(len(board)):
        for column in range(len(board[row])):
            element = board[row][column]
            if element != ".":
                seen_values += [(row, element), (element, column), (element, row // 3, column // 3)]
    return len(seen_values) == len(set(seen_values))

print(bruteValidSudoku([
     ["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]
]))