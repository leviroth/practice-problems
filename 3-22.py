def spin(matrix, n, row, col):
    to_copy = matrix[row][col]
    for _ in range(4):
        new_row = col
        new_col = n - row - 1
        next_to_copy = matrix[new_row][new_col]
        matrix[new_row][new_col] = to_copy
        to_copy = next_to_copy
        row, col = new_row, new_col


def rotate(matrix):
    n = len(matrix)
    row_limit = -(-n // 2)
    col_limit = n // 2
    for row in range(row_limit):
        for col in range(col_limit):
            spin(matrix, n, row, col)


class Solution:
    def rotate(self, matrix):
        rotate(matrix)
