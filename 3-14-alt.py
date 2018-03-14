def get_entry(table, row, col):
    if row < 0 or col < 0:
        return 0
    return table[row][col]


def unique_paths(m, n):
    table = [[1] * n]
    for row in range(1, m):
        new_row = []
        table.append(new_row)
        for col in range(n):
            new_row.append(get_entry(table, row - 1, col)
                           + get_entry(table, row, col - 1))
    return table


class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return unique_paths(m, n)
