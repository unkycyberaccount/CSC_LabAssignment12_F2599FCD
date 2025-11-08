# The program is the 2nd part of the sudoku checking, checking the columns.
# The program sends a sudoku matrix to function `column_check()`,
# the function would check if the specific column is valid.

"""
The followings represent 9 Sudoku blocks.
+-------+-------+-------+
| S . . | S . . | S . . |
| . . . | . . . | . . . |
| . . . | . . . | . . . |
+-------+-------+-------+
| S . . | S . . | S . . |
| . . . | . . . | . . . |
| . . . | . . . | . . . |
+-------+-------+-------+
| S . . | S . . | S . . |
| . . . | . . . | . . . |
| . . . | . . . | . . . |
+-------+-------+-------+

Different with row and column check, we send two index numbers to the function.
They are the starting row index and starting column index of a block.
You can assume that only the starting indices will be sent to the function.

All possible starting indice pair would be:
    (0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3) and (6, 6).
They are marked as "S" in above matrix.
"""


def block_check(sudoku, row_no, column_no):
    """
    Checks if a 3x3 block in a Sudoku grid is valid.
    A block is valid if numbers 1–9 appear at most once (0s are ignored).

    @param sudoku: list of list of int - The Sudoku grid.
    @param row_no: int - The starting row index of the block.
    @param column_no: int - The starting column index of the block.

    @return: bool - True if the block is correct, False otherwise.
    """

    seen = set()  # track numbers in the block

    for i in range(row_no, row_no + 3):
        for j in range(column_no, column_no + 3):
            num = sudoku[i][j]
            if num != 0:  # ignore zeros
                if num in seen:
                    return False  # duplicate found
                seen.add(num)

    return True  # no duplicates found


if __name__ == "__main__":
    sudoku = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2],
    ]

    print(block_check(sudoku, 0, 0))  # False (two 2s in block)
    print(block_check(sudoku, 0, 3))  # True
